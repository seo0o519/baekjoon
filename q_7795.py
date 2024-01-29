numTestCase = int(input())
for _ in range(numTestCase):
    a, b = map(int, input().split())
    a_lst = list(map(int, input().split()))
    a_lst.sort()
    b_lst = list(map(int, input().split()))
    b_lst.sort()

    ans = 0
    j = 0
    for i in range(a):
        while True:
            if j==b or a_lst[i] <= b_lst[j]:
                ans += j
                break
            else: # a>b인 경우
                j += 1


    print(ans)
