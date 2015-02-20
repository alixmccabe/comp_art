""" Synthesizes a blues solo algorithmically """

from Nsound import *
import numpy as np
from random import choice

def add_note(out, instr, key_num, duration, bpm, volume):
    """ Adds a note from the given instrument to the specified stream

        out: the stream to add the note to
        instr: the instrument that should play the note
        key_num: the piano key number (A 440Hzz is 49)
        duration: the duration of the note in beats
        bpm: the tempo of the music
        volume: the volume of the note
	"""
    freq = (2.0**(1/12.0))**(key_num-49)*440.0
    stream = instr.play(duration*(60.0/bpm),freq)
    stream *= volume
    out << stream


def make_lick(instr):

    """ these are the piano key numbers for a 3 octave blues scale in A
    	See: http://en.wikipedia.org/wiki/Blues_scale """
    blues_scale = [25, 28, 30, 31, 32, 35, 37, 40, 42, 43, 44, 47, 49, 52, 54, 55, 56, 59, 61]
    beats_per_minute = 200				# Let's make a slow blues solo

    #making a blues solo for an instrument
    #two licks were added for super-funkyness
    licks = [ [ [1,0.5], [1,0.5*1.1], [1, 0.5*2.9], [1, 0.5] ],[ [1,0.5], [-1,0.5*2.9], [1, 0.5], [-1, 0.5*1.1] ],[ [1,0.5*2], [1,0.5*1.1], [1, 0.5*2.9], [-1, 0.5] ,[1,0.5],[-1,0.5*0.9]] ]
    for i in licks:
        #the second lick generally sounds good as an ending to a series of random licks
        lick = choice(licks) + choice(licks) + choice(licks) +licks[2]
        curr_note = 0

        for note in lick:
            if curr_note >= 0 and curr_note < len(blues_scale)-1:
                curr_note += note[0]
                add_note(solo, instr, blues_scale[curr_note], note[1], beats_per_minute, 1.0)
            else:
                curr_note += note[0]

    return solo

if __name__=="__main__":
    # this controls the sample rate for the sound file you will generate
    sampling_rate = 44100.0
    solo = AudioStream(sampling_rate, 1)
    Wavefile.setDefaults(sampling_rate, 16)
    bass = GuitarBass(sampling_rate)    # use a guitar bass as the first instrument
    piano = OrganPipe(sampling_rate) #use an organ as the second instrument
    
    m = Mixer()
    m.add(0, 0, make_lick(bass))    # add bass guitar and organ pipe for some sick jams  
    m.add(0, 0, make_lick(piano))

    m.getStream(500.0) >> "slow_blues6.wav"
