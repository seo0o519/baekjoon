numTestCase = int(input())
for _ in range(numTestCase):
    num = int(input())
    def fun(num):
        lst = []
        for i in range(2,num+1):
            cnt = 0
            while num%i==0:
                cnt += 1
                num = num/i
            if cnt !=0 :
                lst.append([i,cnt])
        return lst
    ans = fun(num)
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
