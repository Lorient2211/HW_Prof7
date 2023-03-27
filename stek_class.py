class Stekk():
    def __init__(self):
        self.meaning = []

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter >= len(self.meaning):
            raise StopIteration
        else:
            element = self.meaning[self.counter]
            self.counter += 1
            return element

    def is_empty(self):
        return self.meaning == []
        
    def push(self, value):
        self.meaning.append(value)
    
    def peek(self):
        return self.meaning[-1]
    
    def size(self):
        return len(self.meaning)
    
    def pop(self):
        if self.meaning == []:
            return None
        else:
            return self.meaning.pop()
