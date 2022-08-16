for test_case in range(1, 11):
    tc = int(input())
    matrix = []
    for c in range(100):
        list1= list(map(int,input().split()))
        matrix.append(list1)
    summ =summ_col= 0
    sum_list = []
    sum_list_col =[]
    for c in range(100):
        for r in range(100):
            summ += matrix[c][r]
            summ_col += matrix[r][c]
        sum_list.append(summ)
        sum_list_col.append(summ_col)
        summ = summ_col=0
    max_ro = max(sum_list)
    max_co = max(sum_list_col)
    if max_ro > max_co:
        print(f'#{tc} {max_ro}')
    else:
        print(f'#{tc} {max_co}')
