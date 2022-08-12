num_dict ={'0':0, '1': 0, '2': 0, '3': 0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}

mu_num = 1
for i in range(3):
    num = int(input())
    mu_num *=num
mu_num = str(mu_num)
for i in mu_num:
    num_dict[i] +=1
for i in num_dict:
    print(num_dict[i])
