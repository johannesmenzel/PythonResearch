#!/usr/bin/env python3
# from pylab import *
import numpy as np
# import wave # not needed (yet)
# import struct
import matplotlib.pyplot as plt

# CONSTANTS
# Test signal vars
samplerate = 48000.0
numchannels = 2
numsamples = 48000
frequency = 1000.0
amplitude = 1.0
sample = np.arange(0, numsamples, 1)
# Plot vars
plotstart = 0
plotstop = numsamples

# RUNTIME
envDb = 0.0

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
        output[c,s] = input[c,s]
         


# PLOTTING FUNCTION
plt.figure(1)
for c in range(numchannels):
    plt.subplot(211+c)
    plt.plot(sample, input[c,sample], 'b-', sample, output[c,sample], 'r-')
# xticks()
    plt.xlim(( plotstart , plotstop ))
    plt.ylim(( -2.0 , 2.0 ))
    # plt.title( 'channel ' + repr(c) )
    plt.xlabel( 'samples')
    plt.ylabel( 'amp ch ' + repr(c) )
plt.show()