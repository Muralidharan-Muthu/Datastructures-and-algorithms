from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    # push elements into the stack
    def push(self,val):
        self.container.append(val)
    
    # pop last element from the stack
    def pop(self):
        return self.container.pop()
    
    # see the last element in the stack
    def peek(self):
        return self.container[-1]
    
    # to check is our stack memory is empty or not
    def is_empty(self):
        return (self.container) == 0
    
    # to get the size of the stack
    def size(self):
        return len(self.container)
    
    # this will show the all the elements in the stack
    def show(self):
        print(self.container)
    
if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)

    stack.show()
    print(stack.size())
    print(stack.is_empty())

    stack.pop()
    stack.pop()

    stack.show()

    print(stack.peek())
