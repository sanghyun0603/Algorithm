hour,min,sec = map(int,input().split())
oven_sec = int(input())
oven_hour=oven_min=oven_secs = 0
if oven_sec < 3600:
    oven_min = oven_sec//60
    oven_secs = oven_sec -(60*oven_min)
else:
    oven_hour = oven_sec//3600
    oven_min = (oven_sec-(oven_hour*3600))//60
    oven_secs =(oven_sec-(oven_hour*3600)-(60*oven_min))

hour += oven_hour
min += oven_min
sec += oven_secs
if sec > 59:
    min +=1
    sec -=60
if min > 59:
    hour +=1
    min -=60
while hour > 23:
    hour -=24
print(hour,min,sec)

