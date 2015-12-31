from automata import TransitionAutomata, ShadeAutomata
import itertools
from pprint import pprint

class Groove:

    def __init__(self, length=1, repeat=2, transitions=7, staccato=6):
        
        ta = TransitionAutomata()
        sa = ShadeAutomata()

        self.loop = []
        
        subgroove = ta.get_groove(transitions, length)
        epa = [subgroove for r in range(repeat)]
        groove = itertools.chain( *epa )
        self.loop = [int(n) for n in groove]
        
