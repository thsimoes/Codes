def fibonacci(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    i = 2
    while i <= n:
        x = a + b
        a = b
        b = x
        i += 1
    return x

for i in range(10):
    print(fibonacci(i))