num_list = []
for i in range(10):
    N = int(input())
    n = N%42
    if n not in num_list:
        num_list.append(n)
print(len(num_list))