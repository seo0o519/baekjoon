len_A = int(input())
A = list(map(int, input().split()))
order_A = sorted(A)
ans = [-1]*len_A
for i in range(len_A):
    for j in range(len_A):
        if A[i]==order_A[j]:
            ans[i] = j
            order_A[j] = -1
            break

for k in range(len(ans)):
    print(ans[k], end=" ")

