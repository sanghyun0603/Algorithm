T = int(input())
for tc in range(1,T+1):
    N, word = input().split()
    N = int(N)
    for i in word:
        print(i*N,end='')
    print()
