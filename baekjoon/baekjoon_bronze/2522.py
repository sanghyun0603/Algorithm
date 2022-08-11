N= int(input())
for i in range(N):
    print(' '*(N-1-i),end='')
    print('*'*(i+1),end='')
    print()
for i in range(N-1,0,-1):
    print(' '*(N-i),end='')
    print('*'*(i),end='')
    print()