n, kim, im = map(int, input().split())
kim -= 1
im -= 1
round = 0
while kim!=im:
    kim  = kim // 2
    im = im // 2
    round += 1
print(round)