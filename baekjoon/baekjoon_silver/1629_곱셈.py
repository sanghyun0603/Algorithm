def gu(a,b,c):
    if b == 1:
        return a%c
    else:
        val = gu(a,b//2,c)
        if b%2 == 0:
            return val*val%c
        else:
            return val*val*a%c

a,b,c = map(int,input().split())
print(gu(a,b,c))