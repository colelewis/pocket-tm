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