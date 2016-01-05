from automata import TransitionAutomata, ShadeAutomata
import itertools
from pprint import pprint

class Roll:

    def __init__(self, length=1, repeat=2, transitions=7, shade=6):
        
        ta = TransitionAutomata()
        
        subgroove = ta.get_groove(transitions, length)
        epa = [subgroove for r in range(repeat)]
        groove = itertools.chain( *epa )
        self.groove = [int(n) for n in groove]

        sa = ShadeAutomata()
        
        subgroove = sa.get_groove(shade, length)
        groove = itertools.chain( *[subgroove for r in range(repeat)] )
        self.staccato = [int(n) for n in groove]
        
