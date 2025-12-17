class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt


class SinglyLinkedList:
    def __init__(self):
        self.start = None
        self._length = 0
        self.end = None

    def append(self, data):
        new_node = Node(data)
        if self.start is None:  
            self.start = new_node
            self._length += 1
            if self.end is None:
                self.end = new_node
            return

        self.end.nxt = new_node
        self.end = new_node
        self._length += 1

    def prepend(self, data): 
        new_node = Node(data, nxt=self.start)
        self.start = new_node
        if self.end is None:
            self.end = new_node
        self._length += 1

    def insert(self, position, data):
        if position < 0 or position > self._length:
            raise IndexError("index out of range")

        if position == 0:
            self.prepend(data)
            return

        if position == self._length:
            self.append(data)
            return

        current = self.start
        for _ in range(position - 1):
            current = current.nxt

        new_node = Node(data, nxt=current.nxt)
        current.nxt = new_node
        self._length += 1

    def __iter__(self):
        current = self.start
        while current is not None:
            yield current.data
            current = current.nxt

    def __len__(self):
        return self._length

    def __repr__(self):
        items = list(self)
        return f"SinglyLinkedList({items})"
