import sys, json
from src.tape import tape

class tm:
    def __init__(self, input_string):
        self.final_states = []
        self.current_state = 0
        self.blank_symbol = "_" # underscore is used by default, changed by loading configuration
        self.alphabet = []
        self.transitions = {}

        self.parse_transitions()

        self.tape = tape(input_string, self.blank_symbol)
        
        self.render()
        self.compute()
    
    def render(self):
        print("Current state: " + str(self.current_state) + " | Tape: ", end='')
        self.tape.render()

    def pretty_render(self):
        # include self.tape.pretty_render()
        pass

    def parse_transitions(self):
        d = json.load(open(sys.argv[1]))
        self.final_states = d['final_states']
        self.alphabet = d['alphabet']
        self.alphabet += d['blank_symbol']
        self.blank_symbol = d['blank_symbol']
        for i in range (0, len(d['transitions'])):
            current_state = d['transitions'][i]['current_state']
            symbol = d['transitions'][i]['symbol']
            new_state = d['transitions'][i]['new_state']
            write = d['transitions'][i]['write']
            direction = d['transitions'][i]['direction']
            self.transitions[(current_state, symbol)] = (new_state, write, direction)
        
    def compute(self):
        while self.current_state not in self.final_states:
            if ((self.current_state, self.tape.read()) not in self.transitions):
                print("reject") # undefined behavior, no key exists, tm cannot continue
                break
            output_tuple = self.transitions[(self.current_state, self.tape.read())] # reads (current state, current symbol at head) and generates a tuple with (output state, output symbol, direction)
            self.tape.write(output_tuple[1]) # write output symbol to tape
            self.tape.move(output_tuple[2]) # move head the specified direction on the tape
            self.current_state = output_tuple[0] # set current state to output state
            self.render() # render instance of tape
            if (self.current_state in self.final_states):
                print("accept")
                break