hour,mini = map(int,input().split())
cook_mi = int(input())

if mini+cook_mi > 59:
    cook_hour =(mini+cook_mi)//60
    if cook_hour + hour > 23:
        hour = (cook_hour+hour)%24
        mini = (mini+cook_mi)%60
    else:
        hour = (cook_hour)+hour
        mini = (mini+cook_mi)%60
else:
    mini += cook_mi

print(hour,mini)
        