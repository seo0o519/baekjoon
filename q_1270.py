import sys
num = int(input())
ans = 0
for i in range(num):
    data = list(map(int, sys.stdin.readline().split()))
    dict = {}
    for j in range(len(data)):
        if data[j] in dict:
            dict[data[j]] += 1
        else:
            dict[data[j]] = 1

    max_key = max(dict, key=dict.get)
    if dict[max_key] >= len(data)/2.0:
        ans = max_key
    else:
        ans ="SYJKGW"
    print(ans)