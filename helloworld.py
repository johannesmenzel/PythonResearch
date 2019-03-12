#!/usr/bin/env python3

import numpy as np
# import wave # not needed (yet)
# import struct
import matplotlib.pyplot as plt

frequency = 5.0
numsamples = 48000
samplerate = 48000.0
amplitude = 1.0

def testsignal(sample): 
    return [np.sin(2 * np.pi * frequency * sample/samplerate) for sample in range(0, 24000, 1)], [0 for sample in range (numsamples) ]


sample = np.arange(0, numsamples, 1)

plt.figure(1)
plt.subplot(111)
plt.plot(sample, testsignal(sample), 'b-')
plt.show()