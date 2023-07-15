num = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
A = sorted(A)
B = sorted(B, reverse = True)
for i in range(num):
    ans += A[i]*B[i]
print(ans)