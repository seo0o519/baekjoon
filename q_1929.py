def check_prim(n):
    i = 2
    while i*i <= n :
        if n%i==0:
            return False
        i+=1
    return True

m, n = map(int, input().split())

for i in range(m,n+1):
    if check_prim(i):
        if i!=1:
            print(i)
