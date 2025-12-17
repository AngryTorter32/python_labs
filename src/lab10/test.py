from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList


print("Стек")
stack = Stack()
for i in range(10):
    stack.push(i)

while not stack.empty():
    print("peek =", stack.peek(), "pop =", stack.pop())

print("Очередь")

queue = Queue()
for i in range(10):
    queue.enqueue(i)

while not queue.is_empty():
    print("peek =", queue.peek(), "dequeue =", queue.dequeue())

print("Односвязный список")

lst = SinglyLinkedList()

# append
for i in range(3):
    lst.append(i)
print("after append:", list(lst))

# prepend
lst.prepend(-1)
print("after prepend:", list(lst))

# insert
lst.insert(2, 99)
print("after insert:", list(lst))

# insert at edges
lst.insert(0, -2)
lst.insert(len(lst), 3)
print("after edge inserts:", list(lst))

# checks
print("size:", len(lst))
print("start:", lst.start.data)
print("end:", lst.end.data)
