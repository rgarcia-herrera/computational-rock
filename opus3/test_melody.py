from loopseq import Sequencer
import mido
import mingus.core.scales as scales
from mingus.containers import Note
import networkx as nx
import random
from pprint import pprint
from groove import Roll
from melody import Melody, scale2ints, random_walk_edge_weight
from itertools import combinations

# configure scale as list of ints: midi notes
scale = scale2ints(scales.Major, 'A', span=1, octave=2)


# prepare network of intervals
g = nx.barabasi_albert_graph(len(scale), 4)
#g = nx.erdos_renyi_graph(len(scale),0.2)
#g = nx.watts_strogatz_graph(len(scale), 3, 0.3)
random_walk_edge_weight(g)



# create roll object
roll = Roll(length      = 1,
            repeat      = 4,
            transitions = 9,
            shade       = 2)

# bring it all together
m = Melody(scale=scale,
           graph=g,
           length=1,
           repeat=2,
           roll=roll)

print m.loop[0]
# loop = Melody.loop
output = mido.open_output( u'ZynAddSubFX')
s = Sequencer( output, bpm=120, loop=m.loop)

s.play()

