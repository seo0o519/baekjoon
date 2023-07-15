num = int(input())
for i in range(num):
    denom = 1 # 분모
    nume = 1 # 분자
    site = list(map(int, input().split()))
    if site[0] == site[1]:
        ans = 1
    else:
        for j in range(site[0]):
            denom = denom * site[1]
            site[1] = site[1]-1
        while site[0] != 1:
            nume = nume * site[0]
            site[0] = site[0]-1
        ans = denom/nume
    print(int(ans))

