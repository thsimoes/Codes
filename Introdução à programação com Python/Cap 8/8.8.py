def mdc(a,b):
    if b == 0:
        return a
    else:
        x =  a % b
        a = b
        b = x
        return mdc(a,b)

def mmc(a,b):
    return int(abs(a*b)/mdc(a,b))

print(mmc(63,12))