n, tae, p = map(int, input().split()) # n:랭킹에 있는 점수 개수, p:랭킹에 올라갈 수 있는 점수 개수
if n == 0:
    rank_lst = []
else:
    rank_lst = list(map(int, input().split()))
rank_lst.sort(reverse=True)

rank = 1
for i in rank_lst:
    if tae < i:
        rank += 1
    elif tae == i :
        break
    elif tae > i:
        break
if rank > p or (n==p and rank_lst[-1] == tae):
    rank = -1

print(rank)