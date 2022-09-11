# N,K = map(int,input().split())
# cnt = K
# yo = []
# i = 1
# while True:
#     print(yo)
#     if i == cnt:
#         if len(yo) == N:
#             break
#         yo.append(i)
#
#         cnt = (cnt+K)%N
#     if i == N:
#         i = 1
#     i += 1
# print(yo)
#
# T = int(input())
# for tc in range(1,T+1):
#     A,B = map(int,input().split())
#     print(f'Case #{tc}: {A+B}')
import sys
T=int(input())
for tc in range(1,T+1):
    A,B = map(int,sys.stdin.readline)