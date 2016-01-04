import mingus.core.scales as scales
import mingus.core.notes as notes
from mingus.containers import Note
from automata import TransitionAutomata, ShadeAutomata
import itertools
from groove import Roll
import networkx as nx
import matplotlib.pyplot as plt
import random
from pprint import pprint
from midi_ints import midi2note

def scale2ints(minguscale, key='C', span=2, octave=3):
    scale = minguscale(key, span)
    notas = []
    for o in range(octave, octave+span):
        for n in range(7):
            notas.append(int(Note(scale.ascending()[n], o)))
    notas.append(int(Note(scale.tonic, octave+span)))
    return notas


def random_walk_edge_weight(graph):
    n = random.choice(graph.nodes())

    # init weights at 1
    for e in graph.edges():
        graph.add_edge(*e,w=1)

    # jump around hundreds of times
    for i in range(len(graph.edges())*100):
        neighbors = nx.neighbors(graph,n)
        
        if neighbors:
            m = random.choice( neighbors )
        
        w = graph.get_edge_data(n,m)['w']

        graph.add_edge(n,m,w=w+1)
        
        n = m






    

class Melody:


    def random_walk_interval(self, node):
        neighbors = nx.neighbors(self.graph, node)

        if neighbors:
            # create array of choices proportional to edge weights
            choices = []
            for m in neighbors:
                w = self.graph.get_edge_data(node,m)['w']
                for i in range(w):
                    choices.append(m)
                    if random.choice([True, False]):
                        choices.append(node)
        else:
            choices = random.sample(self.graph.nodes(),1)
        return random.choice(choices)

    
    def __init__(self, scale, graph, roll, length=1, repeat=2):

        self.graph = graph
        self.roll  = roll
        self.scale = scale
        self.loop  = [ scale, ]

        submelody = 8
        note = 0
        for i in range(len(self.roll.groove)):
                       
            # render sixteenth
            t = []
            for n in range(len(scale)):
                if self.roll.groove[i] and n == note:
                    t.append(1)
                else:
                    t.append(0)

            s = []
            for n in range(len(scale)):
                if self.roll.staccato[i] and n == note:
                    s.append(1)
                else:
                    s.append(0)
                    
            self.loop.append((t,s))
            # get a new note
            if i < len(self.roll.groove)-1:
                if self.roll.groove[i] == 1 and self.roll.groove[i+1] == 0:
                    note = self.random_walk_interval( note )
        

    def plot_graph(self):
        pos=nx.spring_layout(self.graph, weight='w')

        nx.draw_networkx_nodes(self.graph, pos,
                               node_color='r',
                               node_size=500,
                               alpha=0.8)


        # group edges by their weight
        edgelists = {}
        for e in self.graph.edges():
            w = self.graph.get_edge_data(*e)['w']
            if w in edgelists:
                edgelists[w].append(e)
            else:
                edgelists[w] = [e,]

        # plot edges
        width=1
        for w in edgelists:
            nx.draw_networkx_edges(self.graph,pos,
                                   edgelist=edgelists[w],
                                   width=width,
                                   alpha=0.5,
                                   edge_color='b')
            width+=1

        labels={}
        for n in self.graph.nodes():
            labels[n]=midi2note[self.scale[n]]

        nx.draw_networkx_labels(self.graph,pos,labels,font_size=8)


        plt.axis('off')
        # nx.draw(self.graph)
        plt.savefig("plots/intervals_graph.png")
        



# a specific interval might be e.g. c3-e4, repetition of it makes the
# edge heavier. Create network of intervals from midi file. Random
# walk on this network for melody generation. Also: use network types
# from nx.

# int('11111111', 2)
