T = int(input())
for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))
    sor_list = []
    avg = 0
    for j in range(len(num_list)):
        k = len(num_list) - j
        for i in range(1,k):
            if num_list[i-1] >= num_list[i]:
                temp = num_list[i-1]
                num_list[i-1] = num_list[i]
                num_list[i] = temp
    del num_list[0]
    del num_list[-1]
    for i in range(len(num_list)):
        avg += num_list[i]
    print(f'#{test_case} {int(round(avg/len(num_list),0))}')
