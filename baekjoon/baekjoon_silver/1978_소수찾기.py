def prime(n):                       # 소수찾기문제
    li = [True] *n                  #에라토스테네스의 채를 알려주고 싶다.
    m = int(n**0.5)                 #먼저 입력받은 n만큼의 리스트를 만드는데 모두 소수라 가정(True)
    for i in range(2,m+1):          #n의 약수는 아무리 커야 루트n 이하이다.
        if li[i] == True:           # 해당 숫자가 소수 일때
            for j in range(i+i,n,i): # 그  수의 배수에 해당하는 모든 숫자는 소수가 아니다.
                li[j]=False
    return [i for i in range(2,n) if li[i]== True]# 소수인 숫자만 리스트로 반환한다.

N = int(input())
num_li = list(map(int,input().split()))
max_num = max(num_li)
prime_list = prime(max_num+1)       #N개의 수가 주어지고 소수를 찾는 문제
cnt = 0
for i in num_li:                    #에라토스테네스의 채를 이용 N중 가장 큰수 아래로 소수를 전부 찾은후
    if i in prime_list:             # 비교하여 소수일때만 카운팅
        cnt += 1
print(cnt)