"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.

As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.

The Stack class that you will use has been provided to you.
"""
class Stack:
    def __init__(self):
        self.data = []
        
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"

class QueueTwoStacks:
    def __init__(self):
        self.input_stack = Stack()
        self.output_stack = Stack()
        
    def enqueue(self, item):
        # Your code here
        self.input_stack.push(item)

    def dequeue(self):
        # Your code here
        if len(self.output_stack.data) == 0:
            while len(self.input_stack.data) > 0:
                curr_item = self.imput_stack.pop()
                self.output_stack.push(curr_item)

        if len(self.output_stack.data) == 0:
            return None
        return self.output_stack.pop()