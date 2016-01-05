from time import sleep
import mido


class Sequencer:
    def __init__(self, output, bpm, roll, loop=0):
        self.delay  = 60.0 / (bpm * 4)
        self.roll   = roll
        self.output = output
        self.bar    = 0
        self.t      = 1
        self.loop   = loop



    def play_tine(self):
        for i in range(0,len(self.roll[0])):
            now = self.t
            if self.t == 1:
                prev = len(self.roll) - 1
            else:
                prev = self.t - 1
                        
            # play on 0 to 1
            if (self.roll[prev][0][i] == 0 and self.roll[now][0][i] == 1) or (self.roll[now][0][i] == 1 and self.bar == 0):
                self.output.send(mido.Message('note_on',  note=self.roll[0][i], velocity=64))
            # silence on 1 to 0                        
            elif self.roll[prev][0][i] == 1 and self.roll[now][0][i] == 0:
                self.output.send(mido.Message('note_off', note=self.roll[0][i], velocity=64))
            # 1 to 1?
            elif self.roll[prev][0][i] == 1 and self.roll[now][0][i] == 1:
                # silence and play if staccato part == 0
                if self.roll[prev][1][i] == 0:
                    self.output.send(mido.Message('note_off', note=self.roll[0][i], velocity=64))
                    self.output.send(mido.Message('note_on',  note=self.roll[0][i], velocity=64))                            
    


    def time_delta(self):
        # as time goes by
        print self.roll[self.t] 
        self.bar += 1                
        self.t   += 1
        if self.t == len(self.roll):
            self.t = 1
        sleep(self.delay)
        

    def mute(self):
        for i in range(0,len(self.roll[0])):
            self.output.send(mido.Message('note_off', note=self.roll[0][i], velocity=64))

        
        
    def play(self):
        self.playing = True
        try:
            if self.loop == 0:
                while True:
                    self.play_tine()
                    self.time_delta()
            else:
                for l in range(self.loop):
                    for n in range(len(self.roll)-1):
                        self.play_tine()
                        self.time_delta()
                self.mute()
        except KeyboardInterrupt:
            self.mute()
            exit(0)
