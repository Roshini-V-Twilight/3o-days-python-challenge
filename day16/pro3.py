def fibonacci():
    a = 0
    b = 1

    for i in range(15):
        yield a
        a, b = b, a + b


for num in fibonacci():
    print(num)