from pprint import pprint
from time import sleep
import mido
import random
import mingus.core.scales as scales
from mingus.containers import Note

output = mido.open_output( u'ZynAddSubFX')

loop = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    ]


loop=[ [0,],
       [1,],
       [0,],
       [0,],
       [0,],
       [0,],
       [0,],
       [0,],
       [0,],
       [0,],
       [0,],
       [1,],
       [1,],
       [0,],
       [0,],
       [0,],
       [0,],
       [0,],
       [0,],
       [1,],
       [1,],
       [0,],
       [0,],
       [0,],
       [0,],
       [0,],
       [0,],
       [1,],
       [1,],
       [1,],
       [1,],
       [0,],
       [1,],
       [0,],
       [1,],
       [1,],
       [1,],
       [1,],
       [1,],
       [0,],
       [0,],
       [0,],
       [0,],
       [1,],
       [1,],
       [1,],
       [1,],
       [1,],
       [1,],
       [1,],
       [0,],
       [1,],
       [1,],
       [1,],
       [1,],
       [0,],
       [0,],
       [1,],
       [1,],
       [1,],
       [1,],
       [1,],
       [1,],
       [1,]]

# C3 = 48
escala = scales.HarmonicMajor('C')
escala.octaves = 1
notas = []
for o in range(5,8):
    for n in escala.ascending():
        notas.append(int(Note(n, o)))

bpm = 480
delay = 60.0 / bpm

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

output.close()
