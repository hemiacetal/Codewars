class Automaton(object):

    def __init__(self):
        self.accepts = []
        self.state = 1
        self.automaton = {1:{'0':1, '1':2}, 2:{'0':3, '1':2}, 3:{'0':2, '1':2}}
    
    def transition(self, given):
        self.state = self.automaton[self.state][given]
        
    def __next__(self):
        try:
            Automaton.transition(self, self.accepts.pop(0))
        except IndexError:
            raise StopIteration
            
    def __iter__(self):
        return self
            
    def read_commands(self, commands):
        self.accepts = commands
        for x in self: pass
        return self.state == 2
        
my_automaton = Automaton()