def numbers():
    for i in range(1, 21):
        yield i

for num in numbers():
    print(num)