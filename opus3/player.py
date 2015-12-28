from groove import Groove
from time import sleep
import mido
import random
import mingus.core.scales as scales
from mingus.containers import Note
from pprint import pprint

scale = scales.major('C', 2)

notas = []
for o in range(3,5):
    for n in escala.ascending():
        notas.append(int(Note(n, o)))


class Sequencer:
    def __init__(self, output, scale, octaves, octave, bpm, loop):
        self.delay  = 60.0 / (bpm * 4)
        self.scale  = scale
        self.loop   = loop
        self.output = output


try:
    t = 0
    while True:
        sleep(delay)
        
        for i in range(0,len(loop[t])):
            if loop[t][i]:
                if not loop[t-1][i]:
                    output.send(mido.Message('note_on', note=notas[i], velocity=64))
            else:
                if loop[t-1][i]:
                    output.send(mido.Message('note_off', note=notas[i], velocity=64))

        print loop[t]

        # as time goes by
        t+=1
        if t == len(loop):
            t = 0
        

except KeyboardInterrupt:
    for i in range(0,len(loop[0])):
        output.send(mido.Message('note_off', note=notas[i], velocity=64))
    output.close()

