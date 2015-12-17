from pprint import pprint
from time import sleep
import png
import mido
import random
import mingus.core.scales as scales
from mingus.containers import Note

#output = mido.open_output( u'ZynAddSubFX')


#def groove(bars=1,tension=1):
#    return groove


def transiciones(string):
    """
    suma una transicion cada vez que un caracter cambie en la secuencia del string
    """
    transiciones = 0
    for n in range(1,len(string)):
        if string[n]!=string[n-1]:
            transiciones+=1
    return transiciones


class Groover:

    def __init__(self):

        # sort all 16 bit binary sequences in a regular count
        # from 0000000000000000 to 1111111111111111
        # place that into grooves dict with number of transitions as key
        self.grooves={}
        for n in range(0,1024*64,1):
            string = "{:0>16b}".format(n)
            t = transiciones(string)
            if t in self.grooves:
                self.grooves[t].append(string)
            else:
                self.grooves[t] = [ string, ]


    def get_groove(self,transitions):
        return random.sample(self.grooves[transitions],1)



    def plot_grooves(self):
        s = ['110010010011',
             '101011010100',
             '110010110101',
             '100010010011']


        for t in self.grooves:
            s = self.grooves[t]
            s = map(lambda x: map(int, x), s)            
            with open('%02i.png' % t, 'wb') as f:
                w = png.Writer(len(s[0]), len(s), greyscale=True, bitdepth=1)
                w.write(f, s)


class Agent:

    def __init__(self):
        pass



g = Groover()
g.plot_grooves()
