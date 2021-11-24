a = set([1,2,3,4,5,6])
b = set([1,3,5,7])
c = set()
for i in a:
    if i in b:
        c.add(i)
print(c)
print(b-c)
print(a-c)
