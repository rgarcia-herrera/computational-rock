from loopseq import Sequencer
import mido
import mingus.core.scales as scales
from mingus.containers import Note

from pprint import pprint

# C3 = 48
loop = [
    [48, 50, 52, 53, 55, 57, 59, 60],
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


# scale = scales.Major('C', 2)
# notas = []
# for o in range(3,5):
#     for n in scale.ascending():
#         notas.append(int(Note(n, o)))
# pprint(notas)

output = mido.open_output( u'ZynAddSubFX')

s = Sequencer( output, bpm=60, loop=loop)

s.play()

# s.update_loop( loop )
