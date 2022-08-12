N = int(input())
for i in range(N):
    print(' '*(N-i-1),end='')
    for j in range(1,i+2):
        print('*',end=' ')
    print()