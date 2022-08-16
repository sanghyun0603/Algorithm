T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    revenue = 0
    max_r = 0
    every_revenue = 0
    for sell in range(len(price)-1,-1,-1):
        if max_r < price[sell]:
            max_r = price[sell]
        if max_r > 0:
            revenue += (max_r - price[sell])
            every_revenue += revenue
            revenue =0
    print(f'#{test_case} {every_revenue}')