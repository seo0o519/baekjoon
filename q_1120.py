A, B = input().split()
ans = 0
gap = len(B)-len(A)
lst = []
if len(A) == len(B):
    for i in range(len(A)):
        if A[i]!=B[i]:
            ans += 1
elif A in B:
        ans = 0
else:
    for i in range(gap+1):
        count = 0
        for j in range(len(A)):
            if A[j] != B[i+j]:
                count += 1
        lst.append(count)
    ans = min(lst)
print(ans)




