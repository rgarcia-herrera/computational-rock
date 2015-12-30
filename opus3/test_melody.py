from loopseq import Sequencer
import mido
import mingus.core.scales as scales
from mingus.containers import Note
import networkx as nx
import random
from pprint import pprint

from melody import Melody, scale2ints

scale = scale2ints(scales.Dorian, 'A', span=2, octave=3)
g = nx.barabasi_albert_graph(len(scale), 2)
m = Melody(scale=scale, graph=g, length=1, repeat=2, transitions=7, ):
loop = Melody.loop
output = mido.open_output( u'ZynAddSubFX')
s = Sequencer( output, bpm=40, loop=loop)

s.play()

