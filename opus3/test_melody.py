from loopseq import Sequencer
import mido
import mingus.core.scales as scales
from mingus.containers import Note
import networkx as nx
import random
from pprint import pprint

from melody import Melody, scale2ints, random_walk_edge_weight

# configure scale as list of ints: midi notes
scale = scale2ints(scales.Dorian, 'A', span=2, octave=3)


# prepare network of intervals
g = nx.barabasi_albert_graph(len(scale), 2)
random_walk_edge_weight(g)


# create roll object
roll = Roll(length      = 1,
            repeat      = 2,
            transitions = 7,
            shade       = 6)

# bring it all together
m = Melody(scale=scale,
           graph=g,
           length=1,
           repeat=2,
           roll=roll)

# loop = Melody.loop
# output = mido.open_output( u'ZynAddSubFX')
# s = Sequencer( output, bpm=40, loop=loop)

# s.play()

