import sys

T = int(input())
for tc in range(1,T+1):
    a , b = map(int, sys.stdin.readline().split())
    a = str(a)
    a = int(a[-1])
    if b%4 == 0:
        b = 4
    else:
        b= b%4
    N = a**b
    lit = [10,1,2,3,4,5,6,7,8,9]
    N = str(N)
    print(lit[int(N[-1])])
