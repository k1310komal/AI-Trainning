class stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if len(self.stack) == 0:
           print("stack is empty")
        else:
           return self.stack.pop()

    def peek(self):
         if len(self.stack) == 0:
            print("stack is empty")
         else:
            return self.stack[-1]
    
    def display(self):
        print(self.stack)


s = stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

s.pop()

s.display()

print("Top element:", s.peek())