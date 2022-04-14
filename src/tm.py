import sys, json
from src.tape import tape

class tm:
    def __init__(self):
        self.final_state = 0 # make final_states
        self.current_state = 0
        self.blank_symbol = "_" # underscore is used by default, changed by loading configuration
        self.alphabet = "" # fix w/JSON
        self.transitions = self.parse_transitions()
        # self.transitions = json.load(sys.argv[1])
        self.tape = tape(input("\nInput string: "))

        self.render()
        self.compute()
    
    def render(self):
        print(str(self.current_state) + ":", end='')
        self.tape.render()

    def parse_transitions(self): # rewrite to intake JSON
        lines = []
        d = {}
        with open(sys.argv[1]) as file: 
            lines = file.readlines()
        self.final_state = int(lines[0][29:])
        for x in range (1, len(lines)):
            if (lines[x][0:2].count(' ') != 0 and lines[x][6:8].count(' ') != 0): # single digit input state, single digit output state
                d[(int(lines[x][0:1]), lines[x][2:3])] = (int(lines[x][6:7]), lines[x][8:9], lines[x][10:11])
            elif (lines[x][0:2].count(' ') == 0 and lines[x][7:9].count(' ') != 0): # double digit input state, single digit output state
                d[(int(lines[x][0:2]), lines[x][3:4])] = (int(lines[x][7:8]), lines[x][9:10], lines[x][11:12])
            elif (lines[x][0:2].count(' ') != 0 and lines[x][6:8].count(' ') == 0): # single digit input state, double digit output state
                d[(int(lines[x][0:1]), lines[x][2:3])] = (int(lines[x][6:8]), lines[x][9:10], lines[x][11:12])
            else: # double digit input state, double digit output state
                d[(int(lines[x][0:2]), lines[x][3:4])] = (int(lines[x][7:9]), lines[x][10:11], lines[x][12:13])
        return d

    def compute(self):
        while self.current_state != self.final_state:
            output_tuple = self.transitions[(self.current_state, self.tape.read())] # reads (current state, current symbol at head) and generates a tuple with (output state, output symbol, direction)
            self.tape.write(output_tuple[1]) # write output symbol to tape
            self.tape.move(output_tuple[2]) # move head the specified direction on the tape
            self.current_state = output_tuple[0] # set current state to output state
            self.render() # render instance of tape
            if (self.current_state == self.final_state):
                print("accept") # fix, it has to reject on some input
                break
            elif (self.transitions.get(self.current_state, self.tape.read()) is None):
                print("reject") # undefined behavior
                break