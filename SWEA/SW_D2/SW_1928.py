def bin(n):
    if n ==1 or n==0:
        return str(n)
    else:
        return bin(n//2)+str(n%2)

T = int(input())
for tc in range(1, T + 1):
    table ={word : i for i,word in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')}
    encoding = input()# 입력받은 값을 다시 디코딩하는코드
    mid_phase = []
    result = ''
    for i in encoding :# 인코딩 값을 표에 맞게 숫자로 변환
        mid_phase.append(table[i])
    for j in range(len(mid_phase)):# 후에 이진수로 바꾼다.
        mid_phase[j] =bin(mid_phase[j])# 
        if len(mid_phase[j]) == 1:#바꾸고 난 이진수가 6자리에 맞게 앞에 0을 붙인다.
            mid_phase[j] = '00000'+mid_phase[j]
        elif len(mid_phase[j]) == 2:
            mid_phase[j] = '0000'+mid_phase[j]
        elif len(mid_phase[j]) == 3:
            mid_phase[j] = '000'+mid_phase[j]
        elif len(mid_phase[j]) == 4:
            mid_phase[j] = '00'+mid_phase[j]
        elif len(mid_phase[j]) == 5:
            mid_phase[j] = '0'+mid_phase[j]
        
    binar = ''.join(mid_phase)# 그리고 리스트를 합친다.
    for k in range(0,len(binar),8):#그리고 8자리로 자르고
        temp = binar[k:k+8]
        bi = int(f'0b{temp}',2)# 다시 10진수로 변환
        result += chr(bi)# 아스키코드변환
    print(f'#{tc} {result}')# 문자가 나온다.
