import heapq

numbers = [30, 10, 50, 20, 40]

heapq.heapify(numbers)

smallest = heapq.heappop(numbers)

print("Smallest element:", smallest)