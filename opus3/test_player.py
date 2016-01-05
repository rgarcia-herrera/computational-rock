from loopseq import Sequencer
import mido
import mingus.core.scales as scales
from mingus.containers import Note
import random
from pprint import pprint


scale = scales.Dorian('A', 3)
notas = []
for o in range(2,5):
    for n in scale.ascending():
        notas.append(int(Note(n, o)))
pprint(notas)
ai = random.sample(notas, 8)

# C3 = 48
loop = [
    # [48, 50, 52, 53, 55, 57, 59, 60],
    ai,
    ([0, 0, 0, 0, 0, 0, 0, 1],  [1,1,1,1,1,1,1,1]),
    ([0, 0, 0, 0, 0, 0, 1, 0],  [1,1,1,1,1,1,1,1]),
    
    ([1, 0, 0, 0, 0, 0, 0, 0],  [0,1,1,1,1,1,1,1]),
    ([1, 0, 0, 0, 0, 0, 0, 0],  [0,1,1,1,1,1,1,1]),
    ([1, 0, 0, 0, 0, 0, 0, 0],  [0,1,1,1,1,1,1,1]),
    ([1, 0, 0, 0, 1, 0, 0, 0],  [1,1,1,1,1,1,1,1]),
    ([1, 0, 0, 0, 0, 1, 0, 0],  [1,1,1,1,1,1,1,1]),
    ([1, 0, 0, 0, 0, 0, 1, 0],  [0,1,1,1,1,1,1,1]),
    ([1, 0, 0, 1, 0, 0, 0, 0],  [0,1,1,1,1,1,1,1]),
    ([1, 0, 0, 1, 0, 0, 0, 0],  [0,1,1,1,1,1,1,1]),

    
    ]



output = mido.open_output( u'ZynAddSubFX')

s = Sequencer( output, bpm=40, loop=loop)

s.play()

# s.update_loop( loop )
