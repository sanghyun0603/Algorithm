def cala(N,M) :
    if M == 0:
        return 1
    else:
        return N * cala(N,M-1)
for test_case in range(1, 11):
    T = int(input())
    N,M = map(int,input().split())
    print(f'#{T} {cala(N,M)}')