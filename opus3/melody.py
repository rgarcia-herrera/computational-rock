import mingus.core.scales as scales
from mingus.containers import Note
from automata import TransitionAutomata, ShadeAutomata
import itertools
from groove import Groove
import networkx as nx
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

    def __init__(self, scale, graph, length=1, repeat=2, transitions=7, ):
        g = Groove(length      = length,
                   repeat      = repeat,
                   transitions = transitions)




# scales.ionian("C")


# a specific interval might be e.g. c3-e4, repetition of it makes the
# edge heavier. Create network of intervals from midi file. Random
# walk on this network for melody generation. Also: use network types
# from nx.

# int('11111111', 2)
