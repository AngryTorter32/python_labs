## Лабораторная_10</h1>
### Теория
Стек — линейная структура данных, работающая по принципу LIFO
(последний добавленный элемент извлекается первым).
```
Операции:
push — O(1)
pop — O(1)
peek — O(1)
```

Очередь — линейная структура данных, работающая по принципу FIFO
(первый добавленный элемент извлекается первым).
```
Операции (на базе deque):
enqueue — O(1)
dequeue — O(1)
peek — O(1)
```

Node — элемент связного списка, содержащий значение и ссылку
на следующий узел.
```
Доступ к значению — O(1)
Переход к следующему узлу — O(1)
```

Односвязный список — структура данных, состоящая из узлов,
связанных ссылками.
```
Операции:
append — O(1)
prepend — O(1)
insert — O(n)
доступ по индексу — O(n)
```
### Задание A
```python
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

    def empty(self) -> bool
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
```

### Задание B
```python
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
```
### Тесты
Содержимое test.py:
```python
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
```
Вывод:
<img width="2159" height="1344" alt="lab10_test" src="https://github.com/user-attachments/assets/1f877500-00e1-42f6-b6f5-75918ea97990" />
```
C:\Users\kuzne\Documents\GitHub\python_labs\.venv\Scripts\python.exe C:\Users\kuzne\Documents\GitHub\python_labs\src\lab10\test.py 
Стек
peek = 9 pop = 9
peek = 8 pop = 8
peek = 7 pop = 7
peek = 6 pop = 6
peek = 5 pop = 5
peek = 4 pop = 4
peek = 3 pop = 3
peek = 2 pop = 2
peek = 1 pop = 1
peek = 0 pop = 0
Очередь
peek = 0 dequeue = 0
peek = 1 dequeue = 1
peek = 2 dequeue = 2
peek = 3 dequeue = 3
peek = 4 dequeue = 4
peek = 5 dequeue = 5
peek = 6 dequeue = 6
peek = 7 dequeue = 7
peek = 8 dequeue = 8
peek = 9 dequeue = 9
Односвязный список
after append: [0, 1, 2]
after prepend: [-1, 0, 1, 2]
after insert: [-1, 0, 99, 1, 2]
after edge inserts: [-2, -1, 0, 99, 1, 2, 3]
size: 7
start: -2
end: 3

Process finished with exit code 0
```

Содержимое benchmark.py:
```python
import time
from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList
import random

N = 10000

# Stack тестирование
start = time.perf_counter()
s = Stack()
for i in range(N):
    s.push(i)
for i in range(N):
    s.pop() 
print("Stack:", time.perf_counter() - start)

# Queue тестирование
start = time.perf_counter()
q = Queue()
for i in range(N):
    q.enqueue(i) 
for i in range(N):
    q.dequeue() 
print("Queue:", time.perf_counter() - start)

# Linked list
start = time.perf_counter()
lst = SinglyLinkedList()
for i in range(N):
    lst.append(i)
print("LinkedList append:", time.perf_counter() - start)

# Linked list insert
start = time.perf_counter()
lst = SinglyLinkedList()
for i in range(N):
    lst.insert(i // 2, i)
print("LinkedList insert:", time.perf_counter() - start)
```
Вывод:
<img width="2159" height="1351" alt="lab10_bench" src="https://github.com/user-attachments/assets/8c4dbca8-4ed5-4f03-8e62-be4f0790c918" />
