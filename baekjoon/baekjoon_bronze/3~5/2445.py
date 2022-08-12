N = int(input())
for i in range(N):
    print('*'*(i+1),end='')
    print(' '*((2*N)-(2*(i+1))),end='')
    print('*'*(i+1), end='')
    print()
for i in range(N-1,0,-1):
    print(('*'*i),end='')
    print(' '*((2*N)-(i*2)),end='')
    print('*'*i,end='')
    print()

# 8 6 4 2 0
# 2 4 6 8