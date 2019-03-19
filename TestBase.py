#!/usr/bin/env python3
# from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# CONSTANTS
# Test signal vars
samplerate = 48000.0
numchannels = 2
numsamples = 48000
frequency = 200.0
amplitude = 1.0
sample = np.arange(numsamples)
# Plot vars
plotstart = 9990
plotstop = 11000

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
            input[c,s] = np.sin(2. * np.pi * frequency * s/samplerate)



# PROCESSING PER CHANNEL
for s in range(numsamples):
    for c in range(numchannels):
        output[c,s] = (np.tanh(5. * input[c,s]) / np.tanh(5.)) + input[c,s] - input[c,s-1]


fft = np.fft.fft(output)         
frequencies = np.abs(fft)

# PLOTTING FUNCTION
plt.figure(1)
for c in range(numchannels):
    plt.subplot(211)
    plt.plot(sample, input[c,sample], 'b-', sample, output[c,sample], 'r-')
    # plt.xticks()
    plt.xlim(( plotstart , plotstop ))
    plt.ylim(( -2.0 , 2.0 ))
    plt.title( 'Envelope')
    plt.xlabel( 't(samples)')
    plt.ylabel( 'voltage')
    plt.subplot(223)
    plt.plot(frequencies[c])
    plt.xlim((10, 22000))
    plt.xscale('log')
    plt.title('Response')
    plt.subplot(224)
    plt.scatter(input, output, 1, 'r')
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35) 
plt.show()


fig, ax = plt.subplots() 
plt.subplots_adjust(left=0.25, bottom=0.25) 
t = np.arange(0.0, 1.0, 0.001) 
a0 = 5 
f0 = 3 
delta_f = 5.0 
s = a0*np.sin(2*np.pi*f0*t) 
l, = plt.plot(t, s, lw=2, color='red') 
plt.axis([0, 1, -10, 10]) 
axcolor = 'lightgoldenrodyellow' 
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0, valstep=delta_f)
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0) 

def update(val): 
	amp = samp.val 
	freq = sfreq.val 
	l.set_ydata(amp*np.sin(2*np.pi*freq*t)) 
	fig.canvas.draw_idle() 

sfreq.on_changed(update) 
samp.on_changed(update) 
resetax = plt.axes([0.8, 0.025, 0.1, 0.04]) 
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975') 

def reset(event): 
	sfreq.reset() 
	samp.reset() 
	button.on_clicked(reset) 

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor) 
	
plt.show() 