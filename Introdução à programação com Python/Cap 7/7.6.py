s1 = "AATTCGAA"
s2 = "TG"
s3 = "AC"
n = 0
s4 = list(s1)
for i in s2:
    p = 0
    while p > -1:
        p = s1.find(i,p)
        if p >= 0:
            if n == 0:
                s4[p] = "A"
            else:
                s4[p] = "C"
            p += 1
    n += 1
s4 = "".join(s4)
print(s4)