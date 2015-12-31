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


def random_walk_edge_weight(graph):
    n = None
    for i in range(len(graph.edges())*100):
        if n == None:
            n = random.choice(graph.nodes())

        m = random.choice( nx.neighbors(graph, n) )
        
        if 'w' in graph.get_edge_data(n,m):
            w = graph.get_edge_data(n,m)['w'] + 1
        else:
            w = 1
        graph.add_edge(n,m,w=w)
        n = m






    

class Melody:


    def random_walk_interval(self, node):
        neighbors = nx.neighbors(self.graph, node)
        choices = []
        for m in neighbors:
            w = self.graph.get_edge_data(node,m)['w']
            for i in range(w):
                choices.append(m)
        return random.choice(choices)

    
    def __init__(self, scale, graph, roll, length=1, repeat=2):

        self.graph = graph
        self.roll  = roll
        
        self.loop  = [ scale, ]

        submelody = 8
        note = scale[0]
        for tine in self.roll.groove:
            # render note

            # get a new note
            note = self.random_walk_interval( note )
        
        

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
