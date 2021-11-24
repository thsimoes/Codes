a = set([1, 2, 3, 4])
b = set([2, 4, 6, 8])
c = set()
for i in a:
    if i in b:
        c.add(i)
print(c)
print(a-b)
print(b-a)
d = a|b
print(d-c)
print(a-b)