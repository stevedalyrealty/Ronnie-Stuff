import numpy as np, wave, sys
sys.argv = ['x']
import importlib.util
spec = importlib.util.spec_from_file_location('piano', 'piano.py'); piano = importlib.util.module_from_spec(spec); spec.loader.exec_module(piano)
SR = piano.SR
np.random.seed(7)

def ks_string(freq, dur, damp=0.996, bright=0.5):
    """Karplus-Strong plucked string, computed block by block (fast)."""
    N = max(2, int(round(SR / freq))); n = int(SR * dur)
    buf = (np.random.rand(N) * 2 - 1)
    buf = np.convolve(buf, np.ones(3) / 3, 'same') if bright < 0.5 else buf
    out = np.zeros(n + N); out[:N] = buf; i = N
    while i < n:
        prev = out[i - N:i]; nxt = 0.5 * (prev + np.roll(prev, 1)) * damp
        m = min(N, n - i); out[i:i + m] = nxt[:m]; i += m
    return out[:n]

def power_chord(midi, dur, mute=False, vel=1.0):
    f = 440 * 2 ** ((midi - 69) / 12)
    damp = 0.955 if mute else 0.9965
    strings = [(f, 1.0, 0), (f * 1.5, 0.8, 0.004), (f * 2, 0.6, 0.008)]
    n = int(SR * dur); out = np.zeros(n)
    for fr, a, delay in strings:
        s = ks_string(fr, dur, damp) * a; d = int(delay * SR); out[d:] += s[:n - d]
    # pick attack
    out[:int(SR * 0.004)] *= np.linspace(0.3, 1, int(SR * 0.004))
    return out * vel

def amp(x, gain=9.0):
    y = np.tanh(x * gain) / np.tanh(gain) if gain > 1 else x
    # cab: lowpass-ish via short moving averages, then a touch of presence
    y = np.convolve(y, np.ones(5) / 5, 'same'); y = np.convolve(y, np.ones(3) / 3, 'same')
    return y

def render_guitar(chords, seg, total):
    out = np.zeros(int(total * SR) + SR)
    beat = seg / 4.0; eighth = beat / 2
    def put(t, sig, g=1.0):
        i = int(t * SR); j = min(len(out), i + len(sig)); out[i:j] += sig[:j - i] * g
    for b, (r, q) in enumerate(chords):
        t0 = b * seg
        root = 40 + ((r - 4) % 12)  # E2..D#3 guitar range
        # beat 1: open power chord accent
        put(t0, power_chord(root, beat * 1.6, False, 1.0))
        # chugs: palm-muted eighths with a gallop feel (accent on 1 and the "and" of 2)
        pattern = [None, 0.55, 0.5, 0.75, 0.5, 0.55, 0.5, 0.6]
        for k, v in enumerate(pattern):
            if v is None: continue
            put(t0 + k * eighth, power_chord(root, eighth * 0.95, True, v))
        # riff fill at the end of every other bar: root, b7, 5th, octave
        if b % 2 == 1:
            fill = [(0, 0.0), (10, 0.5), (7, 1.0), (12, 1.5)]
            for semis, pos in fill:
                put(t0 + beat * 3 + pos * eighth, power_chord(root + semis, eighth * 1.1, False, 0.8))
        # every 4th bar: a high harmony stab on the 5th
        if b % 4 == 3:
            put(t0 + beat * 2, power_chord(root + 7, beat * 1.2, False, 0.7))
    return out

# analyze track 2 with the piano module to get the chord map and timing
key, chords = piano.render('music-in/r2_48.wav', 'music-out/ronnie-2.wav', seed=2)
seg = 2.0; dur = len(chords) * seg
g = render_guitar(chords, seg, dur)
g = amp(g, 9.0)
g = g / (np.abs(g).max() + 1e-9)
# stereo: guitar slightly left and doubled slightly right with a 12 ms delay (classic double-track)
d = int(0.012 * SR); gr = np.concatenate([np.zeros(d), g[:-d]])
guitar = np.stack([g * 0.9 + gr * 0.3, g * 0.3 + gr * 0.9], 1)
pno, sr = piano.load_wav('music-out/ronnie-2-piano-only.wav')
n = len(pno); guitar = guitar[:n] if len(guitar) >= n else np.concatenate([guitar, np.zeros((n - len(guitar), 2))])
p_rms = np.sqrt(np.mean(pno ** 2)); g_rms = np.sqrt(np.mean(guitar ** 2))
guitar *= p_rms * 0.85 / g_rms
mix = pno + guitar
mix *= 0.13 / np.sqrt(np.mean(mix ** 2)); mix = np.tanh(mix * 1.1) / np.tanh(1.1); mix *= min(1, 0.92 / np.abs(mix).max())
piano.save_wav('music-out/ronnie-2-fight.wav', mix)
piano.save_wav('music-out/guitar-only.wav', guitar / (np.abs(guitar).max() + 1e-9) * 0.9)
print('key', key, 'bars', len(chords), 'mix rms', round(float(np.sqrt(np.mean(mix ** 2))), 3))
