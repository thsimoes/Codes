s1 = "AATTGGAA"
s2 = "TG"
pos = []
s3 = []
for i in s2:
    n = 0
    while n > -1:
        n = s1.find(i,n)
        if n >= 0:
            pos.append(n)
            n += 1
a = 0
while a < len(s1):
    if a not in pos:
        s3.append(s1[a])
    a += 1
s3 = "".join(s3)
print(s3)