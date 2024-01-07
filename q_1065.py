num = input()
if len(num) <= 2 :
    ans = int(num)
else:
    ans = 99
    for i in range(100, int(num)+1):
        a = i//100
        b = (i%100)//10
        c = i % 10
        if a-b == b-c:
            ans += 1
print(ans)