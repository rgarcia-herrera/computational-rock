import mingus.core.scales as scales
from automata import TransitionAutomata, ShadeAutomata
import itertools
from groove import Groove
from pprint import pprint


class Melody:

    def __init__(self, length=1, repeat=2, transitions=7, scale=scales.ionian("C")):
        g = Groove(length      = length,
                   repeat      = repeat,
                   transitions = transitions)

        int('11111111', 2)

