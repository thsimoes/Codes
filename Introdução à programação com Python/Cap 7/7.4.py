s = "TTAAC"
l = {}
for i in s:
    l[i] = l.get(i,0) + 1
for j in l:
    print(f"{j}: {l[j]}x")