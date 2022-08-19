# N번이 있는 라인 찾기
# 1번 라인 2번라인(2~3) 3번라인(4~6) 4번라인(7~10)
# 5번라인(11~15)
# 짝수라인  분자증가 분모 감소
# 홀수라인 분자감소 분모 증가
N = int(input())
fini = 0
num = 0
while N > fini:             #라인을 끝점을 기준으로 잡는다.
    num += 1                # 라인번호 변수
    fini += num             # 라인값을 끝점에 더해줌
idx = fini -N               # 그 라인에서 N이 몇번째 인덱스인지 찾기
if num%2 == 0:              # 짝수라인과 홀수라인이 증가방식이 다름.
    bunja = num             # 라인값의 끝점을 설정함
    bunmo = 1
    for i in range(idx):    # 그 끝점에서 N의 인덱스가 있는 곳만큼 계산
        bunja -=1
        bunmo +=1
else:                       # 위와 동일하지만 홀수라인은 분자가 증가 분모가 감소
    bunja = 1
    bunmo = num
    for i in range(idx):
        bunja +=1
        bunmo -=1
print(f'{bunja}/{bunmo}')   # 출력력