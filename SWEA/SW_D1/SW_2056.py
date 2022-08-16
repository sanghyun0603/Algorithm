T = int(input())
for test_case in range(1, T + 1):
    a= list(map(int,input()))
    if a[6] > 3:
        print(f'#{test_case} -1')
    elif a[4] > 1 and a[5] > 2:
        print(f'#{test_case} -1')
    elif a[4] == 0 and a[5] ==0 :
        print(f'#{test_case} -1')
    elif a[5] ==2 and a[6] >1 and a[7] > 8:
        print(f'#{test_case} -1')
    elif a[5] ==2 and a[6] >2:
        print(f'#{test_case} -1')
    else:
        b= list(map(str,a))
        year= "".join(b[:4:])
        month = "".join(b[4:6:])
        day = "".join(b[6:8:])
        print(f'#{test_case} {year}/{month}/{day}')