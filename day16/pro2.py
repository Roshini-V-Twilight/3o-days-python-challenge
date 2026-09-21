def odd_numbers():
    for i in range(1, 21):
        if i % 2 != 0:
            yield i

for num in odd_numbers():
    print(num)