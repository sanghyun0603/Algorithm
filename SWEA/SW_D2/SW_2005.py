from math import factorial

import math
T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}')
    N = int(input())
    comb = 0
    for sero in range(N):
        for garo in range(sero+1):
            if garo == 0:
                print(garo+1, end= ' ')
            else:
                comb = math.factorial(sero)/((math.factorial(garo))*(math.factorial(sero-garo)))
                print(int(comb), end= ' ')
        print('')