def bona(n):
    if n == 1 or n == 0:
        return n
    else:
        return bona(n-1)+bona(n-2)
N = int(input())
print(bona(N))