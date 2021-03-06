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
scale = scale2ints(scales.Major, 'C', span=1, octave=3)


# prepare network of intervals
g = nx.barabasi_albert_graph(len(scale), 4)
#g = nx.erdos_renyi_graph(len(scale),0.2)
#g = nx.watts_strogatz_graph(len(scale), 3, 0.3)
random_walk_edge_weight(g)



# create roll object
roll = Roll(length      = 1,
            repeat      = 1,
            transitions = 4,
            shade       = 1)

print roll.groove

# bring it all together
m = Melody(scale=scale,
           graph=g,
           length=1,
           repeat=1,
           roll=roll)

m.plot_graph()

print m.loop[0]
# loop = Melody.loop
output = mido.open_output( u'ZynAddSubFX')
s = Sequencer( output, bpm=120, roll=m.loop, loop=False)

s.play()
s.play()


