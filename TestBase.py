#!/usr/bin/env python3
# from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from fft_test import frequency

# CONSTANTS
# Test signal vars
samplerate = 48000.0
numchannels = 2
numsamples = 48000
frequency = 5000.0
amplitude = 1.0
sample = np.arange(numsamples)
# Plot vars
plotstart = 10000
plotstop = 10000 + 1000 / frequency

# RUNTIME
envDb = 0.0 #for compressor

# BUFFERS
input = np.zeros( (numchannels,numsamples) )
output = np.zeros( (numchannels,numsamples) )

# TEST SIGNAL GENERATION
for s in range(numsamples):
    for c in range(numchannels):
        if s < 10000 or s > 20000:
            input[c,s] = 0.0
        else:
            input[c,s] = np.sin(2 * np.pi * frequency * s/samplerate)



# PROCESSING PER CHANNEL
for s in range(numsamples):
    for c in range(numchannels):
        output[c,s] = np.tanh(5.0 * input[c,s])

fft = np.fft.fft(output)         
frequencies = np.abs(fft)

# PLOTTING FUNCTION
plt.figure(1)
for c in range(numchannels):
    plt.subplot(221+c)
    plt.plot(sample, input[c,sample], 'b-', sample, output[c,sample], 'r-')
    # plt.xticks()
    plt.xlim(( plotstart , plotstop ))
    plt.ylim(( -2.0 , 2.0 ))
    # plt.title( 'channel ' + repr(c) )
    plt.xlabel( 'samples')
    plt.ylabel( 'amp ch ' + repr(c) )
    plt.subplot(223 + c)
    plt.plot(frequencies[c])
    plt.xlim((20, 20000))
plt.show()