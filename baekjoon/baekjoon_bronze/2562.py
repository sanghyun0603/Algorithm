num_list = []
for i in range(9):
    num = int(input())
    num_list.append(num)
maxs = max(num_list)
print(maxs)
print(num_list.index(maxs)+1)
