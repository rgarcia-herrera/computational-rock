from loopseq import Sequencer
import mido
import mingus.core.scales as scales
from mingus.containers import Note
import networkx as nx
import random
from pprint import pprint
from roll import Roll
from melody import Melody, scale2ints, random_walk_edge_weight
from itertools import combinations

# configure some scales as list of ints: midi notes
s0 = scale2ints(scales.Major, 'C', span=4, octave=2)
s1 = scale2ints(scales.NaturalMinor, 'A', span=4, octave=2)



# prepare network of intervals
BA = nx.barabasi_albert_graph(len(s0), 1)
ER = nx.erdos_renyi_graph(len(s0),0.25)
WS = nx.watts_strogatz_graph(len(s0), 3, 0.7)


random_walk_edge_weight(BA)
random_walk_edge_weight(ER)
random_walk_edge_weight(WS)


# create roll objects
r1 = Roll(length      = 1,
          repeat      = 4,
          transitions = 5,
          shade       = 5)
r2 = Roll(length      = 1,
          repeat      = 4,
          transitions = 5,
          shade       = 9)
r3 = Roll(length      = 1,
          repeat      = 4,
          transitions = 5,
          shade       = 8)
r4 = Roll(length      = 4,
          repeat      = 1,
          transitions = 11,
          shade       = 1)

routro = Roll(length      = 4,
              repeat      = 2,
              transitions = 14,
              shade       = 13)


# themes
o  = Melody(scale=s0,
            graph=WS,
            roll=r1)

o_ = Melody(scale=s0,
            graph=ER,
            roll=r1)

p = Melody(scale=s1,
            graph=WS,
            roll=r4)

r = Melody(scale=s1,
            graph=BA,
            roll=r3)

s = Melody(scale=s1,
           graph=BA,
            roll=r2)

r_ = Melody(scale=s0,
            graph=ER,
            roll=r3)

s_ = Melody(scale=s0,
           graph=ER,
            roll=r2)

outro = Melody(scale=s0,
               graph=WS,
               roll=routro)

# loop = Melody.loop
output = mido.open_output( u'ZynAddSubFX')

###################
# |------A------| #
# |--a--| |--b--| #
#  o  o'   o   p  #
#                 #
# |------B------| #
# |--c--| |--d--| #
#  r  s    r' s'  #
###################

pattern = [
    Sequencer( output, bpm=120, roll=o.loop, loop=1),
    Sequencer( output, bpm=120, roll=o_.loop, loop=1),
    Sequencer( output, bpm=120, roll=o.loop, loop=1),
    Sequencer( output, bpm=120, roll=p.loop, loop=1),
    Sequencer( output, bpm=120, roll=r.loop, loop=1),
    Sequencer( output, bpm=120, roll=s_.loop, loop=1),
    Sequencer( output, bpm=120, roll=r_.loop, loop=1),
    Sequencer( output, bpm=120, roll=s_.loop, loop=1),
    Sequencer( output, bpm=120, roll=outro.loop, loop=1),    
]

for theme in pattern:
    theme.play()

output.close()
