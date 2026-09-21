from collections import deque

queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")

print("Queue:", queue)

queue.popleft()

print("After removing:", queue)