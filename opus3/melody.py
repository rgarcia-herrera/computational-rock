import mingus.core.scales as scales
from mingus.containers import Note
from automata import TransitionAutomata, ShadeAutomata
import itertools
from groove import Groove
import networkx as nx
import random
from pprint import pprint


def scale2ints(minguscale, key='C', span=2, octave=3):
    scale = minguscale(key, span)
    notas = []
    for o in range(octave, octave+span):
        for n in range(7):
            notas.append(int(Note(scale.ascending()[n], o)))
    notas.append(int(Note(scale.tonic, octave+span)))
    return notas


class Melody:

    def random_walk_edge_weighter(self):
        n = None
        for i in range(len(self.graph.edges())*100):
            if n == None:
                n = random.sample(self.graph.nodes(),1)[0]
            
            neighbors = nx.neighbors(self.graph, n)
            m = random.sample(neighbors, 1)[0]
            if 'w' in self.graph.get_edge_data(n,m):
                w = self.graph.get_edge_data(n,m)['w'] + 1
            else:
                w = 1
            self.graph.add_edge(n,m,w=w)
            n = m
    
    def __init__(self, scale, graph, length=1, repeat=2, transitions=7, ):
        g = Groove(length      = length,
                   repeat      = repeat,
                   transitions = transitions)

        self.graph = graph
        self.random_walk_edge_weighter()
        self.loop  = [ scale, ]

        

        
    def random_walk_interval(self, node):
        pass
# [
#     # [48, 50, 52, 53, 55, 57, 59, 60],
#     ai,
#     ([0, 0, 0, 0, 0, 0, 0, 1],  [1,1,1,1,1,1,1,1]),
#     ([0, 0, 0, 0, 0, 0, 1, 0],  [1,1,1,1,1,1,1,1]),
    
#     ([1, 0, 0, 0, 0, 0, 0, 0],  [0,1,1,1,1,1,1,1]),
#     ([1, 0, 0, 0, 0, 0, 0, 0],  [0,1,1,1,1,1,1,1]),
#     ([1, 0, 0, 0, 0, 0, 0, 0],  [0,1,1,1,1,1,1,1]),
#     ([1, 0, 0, 0, 1, 0, 0, 0],  [1,1,1,1,1,1,1,1]),
#     ([1, 0, 0, 0, 0, 1, 0, 0],  [1,1,1,1,1,1,1,1]),
#     ([1, 0, 0, 0, 0, 0, 1, 0],  [0,1,1,1,1,1,1,1]),
#     ([1, 0, 0, 1, 0, 0, 0, 0],  [0,1,1,1,1,1,1,1]),
#     ([1, 0, 0, 1, 0, 0, 0, 0],  [0,1,1,1,1,1,1,1]),
#     ]
        


# scales.ionian("C")


# a specific interval might be e.g. c3-e4, repetition of it makes the
# edge heavier. Create network of intervals from midi file. Random
# walk on this network for melody generation. Also: use network types
# from nx.

# int('11111111', 2)
