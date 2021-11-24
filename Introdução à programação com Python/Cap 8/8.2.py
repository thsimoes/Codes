def múltiplo(a,b):
    if a >= b:
        return a % b == 0
    else:
        return b % a == 0

print(múltiplo(8,4))
print(múltiplo(7,3))
print(múltiplo(5,5))