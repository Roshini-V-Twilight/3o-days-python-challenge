from collections import deque

queue = deque()

queue.append("Roshini")
queue.append("Rahul")
queue.append("Priya")
queue.append("Arun")

print("Ticket Booking Queue:")
print(queue)

while queue:
    person = queue.popleft()
    print(person, "ticket booked successfully")