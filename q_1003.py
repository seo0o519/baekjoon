t = int(input())
for _ in range(t):
    n = int(input())
    memo = [-1]*41 #저장할 배열 초기화
    cnt0 = [0]*41
    cnt1 = [0]*41

    def fibonacci(n):
        if memo[n]==-1: # memo에 값이 저장되어 있지 않은 경우
            if n==1 : # 베이스케이스 
                memo[n] = 1
                cnt1[n] +=1
            elif n==0 :
                memo[n] = 0
                cnt0[n] += 1

            else : 
                memo[n] = fibonacci(n-1) + fibonacci(n-2)
                cnt1[n] = cnt1[n-1] + cnt1[n-2]
                cnt0[n] = cnt0[n-1] + cnt0[n-2]
            
        return memo[n]

    fibonacci(n)
    print(cnt0[n], cnt1[n])