from collections import deque

class Stack:
    def __init__(self):
        self.container = []

    def push(self, element):
        self.container.append(element)

    def pop(self):
        if self.empty():
            return None
        return self.container.pop()

    def peek(self):
        if self.empty():
            return None
        return self.container[-1]

    def empty(self) -> bool:
        return not self.container


class Queue:
    def __init__(self):
        self.elements = deque() 

    def enqueue(self, value):
        self.elements.append(value)

    def dequeue(self):
        if not self.elements:
            return None
        return self.elements.popleft()

    def peek(self):
        if not self.elements:
            return None
        return self.elements[0]

    def is_empty(self) -> bool:
        return len(self.elements) == 0
