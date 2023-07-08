white = [1,1,2,2,2,8]
num_list = list(map(int, input().split()))
ans = [0] * len(white)
for j in range(len(white)):
    ans[j] = white[j] - num_list[j]

for k in range(len(ans)):
    print(ans[k], end=" ")



