ha_list = []
be_list = []
for i in range(5):
    menu = int(input())
    if i <3:
        ha_list.append(menu)
    else:
        be_list.append(menu)
print(min(ha_list)+min(be_list)-50)