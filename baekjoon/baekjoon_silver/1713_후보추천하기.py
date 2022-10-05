N = int(input())
chu = int(input())
chu_dict = {}           # 보자마자 딕셔너리나 셋 생각 (서칭이 O(1)이라)
                        # 추천받은 횟수를 증가시켜야함 -> set은 불가능
                        # 그러면? 딕셔너리로 쇼부보자
chu_li = list(map(int,input().split()))
cnt = 0
for i in range(chu):
    if cnt < N:         # 처음 사진틀이 다찰때가진 삭제작업 할필요없음.
        if chu_li[i] in chu_dict:   # 이미 사진틀에 있다면 추천횟수 +1
            chu_dict[chu_li[i]] += 1
        else:
            chu_dict[chu_li[i]] = 1 # 없는 뉴페이스인경우 사진틀에 추가후 카운트증가
            cnt += 1
    else:                           # 사진틀이 꽉차버린 상황
        if chu_li[i] in chu_dict:   # 꽉차버렸지만 사진틀에 있는 애가 나오면 +1 O(1)
            chu_dict[chu_li[i]] +=1
        else:                       # 없는애가 나왔다. 그럼 최소값중 가장 오래된 사진이랑 바꿈
            keys = min(chu_dict,key=chu_dict.get) # 최소값찾는 과정-> 왼쪽부터 찾아서 자동으로 오래된사진이됨
            del chu_dict[keys]                   # 그걸 바탕으로 해당 딕셔너리 삭제후
            chu_dict[chu_li[i]] = 1              # 값추가
ch = sorted(chu_dict.keys())                     # 출력이 오름차순이라 정렬
print(*ch)


