from collections import deque

list = ["b","c","d"]
deq = deque(list)
print(deq)

#inserting elements
deq.append("e")
deq.appendleft("a")
print(deq)

#removing elements
deq.pop()
deq.popleft()
print(deq)

#Clear Deque
deq.clear()
print(deq)

#Counting Elements
list = ["a","a","b","c"]
deq = deque(list)
print(deq.count("a"))

