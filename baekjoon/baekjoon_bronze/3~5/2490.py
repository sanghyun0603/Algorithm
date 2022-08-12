yu_list = []
for i in range(3):
    a = list(map(int,input().split()))
    yu_list.append(a)
for i in yu_list:
    bae = i.count(0)
    dm = i.count(1)
    if bae == 1:
        print('A')
    elif bae == 2:
        print('B')
    elif bae == 3:
        print('C')
    elif bae == 4:
        print('D')
    elif dm == 4:
        print('E')