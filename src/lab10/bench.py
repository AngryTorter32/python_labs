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
