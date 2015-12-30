from groove import Groove
from time import sleep
import mido


class Sequencer:
    def __init__(self, output, bpm, loop):
        self.delay  = 60.0 / (bpm * 4)
        self.loop   = loop
        self.output = output


    def play(self):
        try:
            t = 1
            while True:
                
                for i in range(0,len(self.loop[0])):
                    now = t
                    if t == 1:
                        prev = len(self.loop) - 1
                    else:
                        prev = t - 1
                        
                    # play on 0 to 1
                    if self.loop[prev][0][i] == 0 and self.loop[now][0][i] == 1:
                        self.output.send(mido.Message('note_on',  note=self.loop[0][i], velocity=64))
                    # silence on 1 to 0                        
                    elif self.loop[prev][0][i] == 1 and self.loop[now][0][i] == 0:
                        self.output.send(mido.Message('note_off', note=self.loop[0][i], velocity=64))
                    # 1 to 1?
                    elif self.loop[prev][0][i] == 1 and self.loop[now][0][i] == 1:
                        # silence and play if staccato part == 0
                        if self.loop[prev][1][i] == 0:
                            self.output.send(mido.Message('note_off', note=self.loop[0][i], velocity=64))
                            self.output.send(mido.Message('note_on',  note=self.loop[0][i], velocity=64))                            

                print self.loop[t]

                # as time goes by
                t+=1
                if t == len(self.loop):
                    t = 1
                sleep(self.delay)
        

        except KeyboardInterrupt:
            for i in range(0,len(self.loop[0])):
                self.output.send(mido.Message('note_off', note=self.loop[0][i], velocity=64))
            self.output.close()

