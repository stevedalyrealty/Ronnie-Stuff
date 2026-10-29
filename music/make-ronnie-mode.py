# Original martial-arts disco theme for Ronnie-Mode (not a copy of any existing song): four-on-the-floor drums,
# octave-bouncing bass, a pentatonic plucked lead, brass stabs, a gong and a "HA!" shout. 120 BPM, 24 bars, loops.
import numpy as np, wave
SR = 48000; BPM = 124; BEAT = 60 / BPM; BARS = 24
np.random.seed(3)
T = BARS * 4 * BEAT
out = np.zeros((int(T * SR) + SR, 2))
def put(t, sig, pan=0.0, g=1.0):
    i = int(t * SR); j = min(len(out), i + len(sig)); s = sig[:j - i] * g
    l, r = np.sqrt(0.5 - pan / 2), np.sqrt(0.5 + pan / 2); out[i:j, 0] += s * l; out[i:j, 1] += s * r
def env(n, a, d, sus=0.0, r=0.0, hold=0):
    e = np.ones(n); A = int(a * SR); D = int(d * SR); R = int(r * SR)
    if A: e[:A] = np.linspace(0, 1, A)
    if D: e[A:A + D] = np.linspace(1, sus, D)[:max(0, n - A)]
    e[A + D:] = sus
    if R and n > R: e[-R:] *= np.linspace(1, 0, R)
    return e
def kick(): n = int(0.35 * SR); t = np.arange(n) / SR; f = 50 + 110 * np.exp(-t * 28); return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9) * 1.2
def snare(): n = int(0.22 * SR); t = np.arange(n) / SR; return (np.random.randn(n) * np.exp(-t * 18) * 0.7 + np.sin(2 * np.pi * 190 * t) * np.exp(-t * 30) * 0.6)
def hat(open_=False): n = int((0.3 if open_ else 0.06) * SR); t = np.arange(n) / SR; x = np.random.randn(n); x = x - np.convolve(x, np.ones(8) / 8, 'same'); return x * np.exp(-t * (6 if open_ else 60)) * 0.35
def saw(f, n): t = np.arange(n) / SR; return 2 * ((t * f) % 1) - 1
def square(f, n): t = np.arange(n) / SR; return np.sign(np.sin(2 * np.pi * f * t))
def pluck(f, dur, damp=0.995):
    N = max(2, int(round(SR / f))); n = int(SR * dur); buf = np.random.rand(N) * 2 - 1; o = np.zeros(n + N); o[:N] = buf; i = N
    while i < n: prev = o[i - N:i]; nxt = 0.5 * (prev + np.roll(prev, 1)) * damp; m = min(N, n - i); o[i:i + m] = nxt[:m]; i += m
    return o[:n]
def gong():
    n = int(3.0 * SR); t = np.arange(n) / SR; s = np.zeros(n)
    for f, a in [(98, 1), (147, .6), (196, .5), (262, .35), (330, .25), (440, .15)]: s += a * np.sin(2 * np.pi * f * t + np.sin(2 * np.pi * 3.1 * t) * 0.6) * np.exp(-t * (0.9 + f / 400))
    return s * (1 - np.exp(-t * 200)) * 0.5 + np.random.randn(n) * np.exp(-t * 40) * 0.15
def shout():  # a percussive "HA!" built from a vowel-shaped noise burst
    n = int(0.28 * SR); t = np.arange(n) / SR; x = np.random.randn(n)
    tone = np.sin(2 * np.pi * (220 - 90 * t) * t) * 0.5 + np.sin(2 * np.pi * (660 - 200 * t) * t) * 0.25
    x = np.convolve(x, np.ones(12) / 12, 'same') * 0.6 + tone; return x * env(n, 0.01, 0.2, 0.0) * 1.1
f_of = lambda m: 440 * 2 ** ((m - 69) / 12)
A, C, D, E, G = 57, 60, 62, 64, 67  # A minor pentatonic (A3 based)
chords = [[A, C, E], [G - 12 + 12, 71, 74], [A, C, E], [C, E, G]]  # Am, G, Am, C
for bar in range(BARS):
    t0 = bar * 4 * BEAT
    # drums: disco
    for b in range(4):
        put(t0 + b * BEAT, kick(), 0, 0.9)
        if b in (1, 3): put(t0 + b * BEAT, snare(), 0.1, 0.8)
        put(t0 + b * BEAT, hat(), -0.3, 0.6); put(t0 + b * BEAT + BEAT / 2, hat(True), -0.3, 0.55)
    # bass: root, octave bounce in eighths, walk on the last beat
    ch = chords[bar % 4]; root = ch[0] - 24
    patt = [0, 12, 0, 12, 0, 12, 7, 10] if bar % 4 != 3 else [0, 12, 0, 12, 3, 5, 7, 10]
    for k, semi in enumerate(patt):
        n = int(BEAT / 2 * 0.9 * SR); s = (saw(f_of(root + semi), n) * 0.5 + square(f_of(root + semi) / 2, n) * 0.3) * env(n, 0.004, 0.15, 0.5, 0.03)
        s = np.convolve(s, np.ones(24) / 24, 'same'); put(t0 + k * BEAT / 2, s, 0, 0.45)
    # brass stabs every other bar: beat 1 and the "and" of 2
    if bar % 2 == 0:
        for tt in (0, 1.5 * BEAT):
            n = int(0.22 * SR); s = sum(saw(f_of(m), n) for m in ch) * env(n, 0.01, 0.15, 0.3, 0.03); s = np.convolve(s, np.ones(10) / 10, 'same'); put(t0 + tt, s, 0.25, 0.18)
    # lead: plucked pentatonic riff, 4-bar phrase
    phrase = [[(A + 12, 0), (C + 12, .5), (D + 12, 1), (E + 12, 1.5), (D + 12, 2.5), (C + 12, 3), (A + 12, 3.5)],
              [(G + 12, 0), (A + 12, .5), (C + 12, 1), (A + 12, 2), (G + 12, 2.5), (E + 12, 3)],
              [(A + 12, 0), (C + 12, .5), (D + 12, 1), (E + 12, 1.5), (G + 12, 2), (E + 12, 2.5), (D + 12, 3), (C + 12, 3.5)],
              [(A + 12, 0), (E + 12, 1), (D + 12, 1.5), (C + 12, 2), (A + 12, 3)]][bar % 4]
    if bar >= 4 or bar % 4 >= 2:  # the first bars let the gong and drums breathe
        for m, pos in phrase:
            oct_ = 12 if (bar // 8) % 2 == 1 else 0
            s = pluck(f_of(m + oct_), 0.5, 0.993); put(t0 + pos * BEAT, s, 0.3, 0.5)
            if bar >= 16: put(t0 + pos * BEAT + 0.01, pluck(f_of(m + oct_ - 12), 0.5, 0.993), -0.3, 0.3)
    # gong and shout
    if bar % 12 == 0: put(t0, gong(), 0, 0.9)
    if bar % 4 == 3: put(t0 + 3 * BEAT, shout(), 0, 0.55)
out = out[:int(T * SR)]
out *= 0.14 / np.sqrt(np.mean(out ** 2)); out = np.tanh(out * 1.2) / np.tanh(1.2); out *= min(1, 0.92 / np.abs(out).max())
x = np.clip(out, -1, 1); w = wave.open('music-out/ronnie-mode.wav', 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x * 32767).astype(np.int16).tobytes()); w.close()
print('ronnie-mode', round(T, 1), 's rms', round(float(np.sqrt(np.mean(out ** 2))), 3))
