# Written by Cole Lewis, 2022

import sys

class tm:
    def __init__(self):
        self.final_state = 0
        self.current_state = 0
        self.transitions = self.parse_transitions()
        self.tape = tape(input())
        self.render()
        self.compute()
    
    def render(self):
        print(str(self.current_state) + ":", end='')
        self.tape.render()

    def parse_transitions(self): # very, VERY particular to specified  
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
    
class tape:
    def __init__(self, input):
        self.head = 0
        self.record = self.init_tape(input)

    def init_tape(self, input):
        l = list()
        for x in range(0, len(list(input))):
            l.append(list(input)[x])
        return l

    def read(self):
        return self.record[self.head] # return symbol at head position in tape
    
    def write(self, input_symbol):
        self.record[self.head] = input_symbol

    def move(self, direction):
        if (direction == "<"):
            self.head -= 1
            self.grow() # a conditional is in grow(), calls everytime to check if the tape should grow
        elif (direction == ">"):
            self.head += 1
            self.grow()
        
    def render(self):
        for x in range(0, len(self.record)):
            if x == self.head:
                print('(' + self.record[x] + ')', end = '')
            else:
                print(self.record[x], end = '')
        print('\r')

    def grow(self):
        if (self.head >= len(self.record)):
            self.head = len(self.record)
            self.record.append('_')
        elif (self.head < 0):
            self.record.insert(0, '_')
            self.head = 0
    
    def trim(self): # gets rid of unnecessary blanks to adhere to rubric output format
        for x in range(0, len(self.record)):
            if (self.record[x] == '_' and x != self.head):
                del self.record[x]
            elif (self.record[x] == '_' and x == self.head):
                pass
                

def main():
    if (len(sys.argv) != 2):
        print("Error: too many arguments.\nUsage: python3 tm.py <description text file path>")
        exit(0)
    while True:
        t = tm()
if __name__=="__main__":
    main()
    


    



        