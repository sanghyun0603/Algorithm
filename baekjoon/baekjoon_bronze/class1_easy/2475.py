num_list = list(map(int,input().split()))
for i in range(len(num_list)):
    num_list[i] = num_list[i]**2
print(sum(num_list)%10)