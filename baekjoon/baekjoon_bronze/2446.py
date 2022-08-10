N = int(input())
for i in range(N):
    print(' '*i,end='')
    print('*'*(2*(N-i)-1),end='')
    print()
for i in range(2,N+1):
    print(' '*(N-i) ,end='')
    print('*'*(2*i-1),end='')
    print()