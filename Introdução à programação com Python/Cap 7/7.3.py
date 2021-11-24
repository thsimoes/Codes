s1 = "CTA"
s2 = "ABC"
s3 = []
for i in s2:
    if i not in s1:
        s3.append(i)
for j in s1:
    if j not in s2:
        s3.append(j)
s3 = "".join(s3)
print(s3)