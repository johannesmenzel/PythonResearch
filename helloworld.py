#!/usr/bin/env python3

import numpy as np
# import wave # not needed (yet)
import struct
import matplotlib.pyplot as plt

frequency = 5000
numsamples = 48000
samplerate = 48000.0
amplitude = 1.0

def testsignal(sample): 
    return np.sin(2 * np.pi * frequency * sample/samplerate)


def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)

sample = np.arange(0.0, 48000.0, 1.0)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(221)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(222)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.subplot(223)
plt.plot(sample, testsignal(sample), 'r--')
plt.show()