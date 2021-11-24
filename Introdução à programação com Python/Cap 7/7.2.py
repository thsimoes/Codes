s1 = "AAACTBF"
s2 = "CBT"
s3 = []
for i in s2:
    if i in s1:
        s3.append(i)
s3 = "".join(s3)
print(s3)