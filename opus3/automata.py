from pprint import pprint
from time import sleep
import png
import mido
import random
import itertools
import mingus.core.scales as scales
from mingus.containers import Note

#output = mido.open_output( u'ZynAddSubFX')


#def groove(bars=1,tension=1):
#    return groove
    


class TransitionAutomata:

    
    def transiciones(self, string):
        """
        suma una transicion cada vez que un caracter cambie en la secuencia del string
        """
        transiciones = 0
        for n in range(1,len(string)):
            if string[n]!=string[n-1]:
                transiciones+=1
        return transiciones

    
    def __init__(self):

        # sort all 16 bit binary sequences in a regular count
        # from 0000000000000000 to 1111111111111111
        # place that into grooves dict with number of transitions as key
        self.grooves={}
        for n in range(0,1024*64,1):
            string = "{:0>16b}".format(n)
            t = self.transiciones(string)
            if t in self.grooves:
                self.grooves[t].append(string)
            else:
                self.grooves[t] = [ string, ]



    def get_groove(self,transitions, length):
        return [int(n) for n in itertools.chain(*random.sample(self.grooves[transitions],length))]

    
class ShadeAutomata:

    def zero_count(self,string):
        """
        return number of zeroes in string
        """
        return string.count('0')

    
    def __init__(self):
        # binary count from 0000000000000000 to 1111111111111111
        # sort them by shade, id est: zero count in word
        self.grooves={}
        for n in range(0,1024*64,1):
            string = "{:0>16b}".format(n)
            shade = self.zero_count(string)
            if shade in self.grooves:
                self.grooves[shade].append(string)
            else:
                self.grooves[shade] = [string, ]

                
    def get_groove(self,shade):
        return random.sample(self.grooves[shade],1)







def plot_grooves(grooves, prefix):
    for t in grooves:
        s = grooves[t]
        s = map(lambda x: map(int, x), s)            
        with open('%s_%02i.png' % (prefix,t), 'wb') as f:
            w = png.Writer(len(s[0]), len(s), greyscale=True, bitdepth=1)
            w.write(f, s)

                





# ta = TransitionAutomata()
# sa = ShadeAutomata()

# #plot_grooves(ta.grooves, 'ta')
# #plot_grooves(sa.grooves, 'sa')

# for n in range(15):
#     print sa.get_groove(7)
#     print ta.get_groove(n)
