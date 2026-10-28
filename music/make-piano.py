import numpy as np, wave, sys, struct
SR = 48000
MELODY_GAIN = 1.6
NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

def load_wav(p):
    w = wave.open(p); n = w.getnframes(); ch = w.getnchannels(); sr = w.getframerate()
    d = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768
    return d.reshape(-1, ch), sr
def save_wav(p, x):
    x = np.clip(x, -1, 1); w = wave.open(p, 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((x * 32767).astype(np.int16).tobytes()); w.close()

def analyze(mono, sr):
    N, H = 4096, 1024
    frames = np.lib.stride_tricks.sliding_window_view(mono, N)[::H] * np.hanning(N)
    S = np.abs(np.fft.rfft(frames, axis=1)); freqs = np.fft.rfftfreq(N, 1 / sr)
    mask = (freqs > 70) & (freqs < 2200); midi = 69 + 12 * np.log2(freqs[mask] / 440); pc = np.round(midi).astype(int) % 12
    chroma = np.zeros((S.shape[0], 12)); Sm = S[:, mask] ** 0.5
    for k in range(12): chroma[:, k] = Sm[:, pc == k].sum(1)
    energy = S.sum(1); fps = sr / H
    # key
    cm = chroma.mean(0); cm /= cm.sum()
    major = np.array([6.35,2.23,3.48,2.33,4.38,4.09,2.52,5.19,2.39,3.66,2.29,2.88]); minor = np.array([6.33,2.68,3.52,5.38,2.60,3.53,2.54,4.75,3.98,2.69,3.34,3.17])
    best = max(((np.corrcoef(cm, np.roll(prof, t))[0, 1], t, m) for t in range(12) for prof, m in ((major, 'major'), (minor, 'minor'))))
    # onsets (spectral flux, adaptive threshold)
    flux = np.maximum(0, np.diff(S, axis=0)).sum(1); flux = np.concatenate([[0], flux])
    thr = np.convolve(flux, np.ones(9) / 9, 'same') * 1.6 + flux.max() * 0.04
    on = [i for i in range(1, len(flux) - 1) if flux[i] > thr[i] and flux[i] >= flux[i - 1] and flux[i] >= flux[i + 1]]
    return chroma, energy, fps, best, on

def diatonic(root, mode):
    steps = [0, 2, 4, 5, 7, 9, 11] if mode == 'major' else [0, 2, 3, 5, 7, 8, 10]
    qual = ['maj','min','min','maj','maj','min','dim'] if mode == 'major' else ['min','dim','maj','min','min','maj','maj']
    out = []
    for s, q in zip(steps, qual):
        if q == 'dim': continue
        out.append(((root + s) % 12, q))
    return out

def chord_pcs(r, q): return [(r) % 12, (r + (4 if q == 'maj' else 3)) % 12, (r + 7) % 12]

def piano_note(freq, dur, vel=0.5, sr=SR):
    n = int(sr * dur); t = np.arange(n) / sr
    decay = 1.8 + freq / 300.0  # higher notes die faster
    env = np.exp(-t * decay) * (1 - np.exp(-t * 400))
    out = np.zeros(n)
    amps = [1.0, 0.55, 0.3, 0.2, 0.12, 0.08, 0.05]
    for k, a in enumerate(amps, 1):
        f = freq * k * (1 + 0.0004 * k * k)
        if f > sr / 2.2: break
        out += a * np.sin(2 * np.pi * f * t + 0.3 * k) * np.exp(-t * (decay * 0.5 * k))
    out += 0.03 * np.sin(2 * np.pi * freq * 2.01 * t) * np.exp(-t * 6)  # slight shimmer
    out *= env * vel / 1.6
    # tiny hammer thump
    hn = min(n, int(sr * 0.012)); out[:hn] += (np.random.rand(hn) - 0.5) * 0.08 * vel * np.linspace(1, 0, hn)
    return out

def render(track_path, out_wav, seed=1):
    np.random.seed(seed)
    x, sr = load_wav(track_path); mono = x.mean(1)
    chroma, energy, fps, (corr, root, mode), onsets = analyze(mono, sr)
    print(f'{track_path}: key {NAMES[root]} {mode} (corr {corr:.2f}), {len(onsets)} onsets, {len(mono)/sr:.1f}s')
    palette = [(r, q) for r in range(12) for q in ('maj', 'min')]  # the melody wanders, so follow it chord by chord
    dur = len(mono) / sr
    seg = 2.0  # seconds per chord decision
    nseg = int(np.ceil(dur / seg))
    chords = []; prev = None
    for s in range(nseg):
        a, b = int(s * seg * fps), int(min(len(chroma), (s + 1) * seg * fps))
        c = chroma[a:b].sum(0) if b > a else chroma.mean(0)
        c = c / (c.sum() + 1e-9)
        best, bs = None, -1
        for r, q in palette:
            pcs = chord_pcs(r, q); shared = len(set(pcs) & set(chord_pcs(*prev))) if prev else 0
            score = c[pcs[0]] * 1.3 + c[pcs[1]] + c[pcs[2]] + (0.012 if (r, q) == prev else 0) + 0.006 * shared
            if score > bs: bs, best = score, (r, q)
        if energy[a:b].sum() < energy.mean() * 0.15 * (b - a) and prev: best = prev  # quiet stretch: hold the chord
        chords.append(best); prev = best
    print('  chords:', ' '.join(NAMES[r] + ('' if q == 'maj' else 'm') for r, q in chords))
    out = np.zeros((int(dur * sr) + sr * 4, 2))
    def add(t, midi, d, vel):
        i = int(t * sr); f = 440 * 2 ** ((midi - 69) / 12); note = piano_note(f, d, vel); j = min(len(out), i + len(note))
        pan = np.clip((midi - 60) / 36, -0.6, 0.6); l, r = np.sqrt(0.5 - pan / 2), np.sqrt(0.5 + pan / 2)
        out[i:j, 0] += note[:j - i] * l; out[i:j, 1] += note[:j - i] * r
    # bed: for each 2s segment, a low root on beat 1, then a gentle broken chord (root-5th-3rd-octave) spaced evenly
    for s, (r, q) in enumerate(chords):
        t0 = s * seg
        bass = 36 + r if r >= 5 else 48 + r - 12 + 12  # keep bass around C2..B2
        bass = 36 + ((r - 0) % 12); 
        if bass < 36: bass += 12
        add(t0, bass, 2.4, 0.42)
        third = r + (4 if q == 'maj' else 3)
        voices = [60 + r % 12, 60 + (r + 7) % 12 + (0 if (r + 7) % 12 > r % 12 else 12), 60 + third % 12 + (0 if third % 12 > r % 12 else 12), 72 + r % 12]
        for k, m in enumerate(voices):
            add(t0 + 0.5 * (k + 0.5) * (seg / 2), m, 1.6, 0.26 + 0.04 * np.random.rand())
    # doubling: on strong onsets, play the chord tone closest to the loudest pitch class at that moment
    last = -1
    for o in onsets:
        t = o / fps
        if t - last < 0.22: continue
        last = t
        s = min(len(chords) - 1, int(t / seg)); r, q = chords[s]; pcs = chord_pcs(r, q)
        c = chroma[o]; pc = int(np.argmax(c))
        # nearest chord pitch class
        midi = 60 + pc
        if pc not in pcs: midi = 60 + min(pcs, key=lambda p: min((p - pc) % 12, (pc - p) % 12)) if np.random.rand() < 0.5 else midi
        vel = 0.22 + 0.28 * min(1, energy[o] / (np.percentile(energy, 95) + 1e-9))
        add(t, midi, 1.4, vel * MELODY_GAIN)
    out = out[:len(mono)]
    # level: piano RMS ~ 55% of the recording's RMS, then mix
    rec_rms = np.sqrt(np.mean(x ** 2)); p_rms = np.sqrt(np.mean(out ** 2)) + 1e-9
    piano = out * (rec_rms * 0.55 / p_rms)
    solo = out * (0.09 / p_rms)  # piano alone, normalized to a comfortable level
    mix = x + piano
    mix = np.tanh(mix * 1.1) / np.tanh(1.1)  # gentle soft limiter
    mix *= 0.92 / max(0.92, np.abs(mix).max())
    save_wav(out_wav, mix)
    solo = np.tanh(solo * 1.05) / np.tanh(1.05); solo *= min(1, 0.9 / max(1e-6, np.abs(solo).max())); save_wav(out_wav.replace('.wav', '-piano-only.wav'), solo)
    return NAMES[root] + ' ' + mode, chords

if __name__ == '__main__':
    for i in (1, 2):
        render(f'music-in/r{i}_48.wav', f'music-out/ronnie-{i}.wav', seed=i)
