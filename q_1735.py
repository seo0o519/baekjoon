def gcd(a,b): # 최대공약수 구하는 함수 (유클리드 알고리즘)
    if b==0:
        return a
    else:
        return gcd(b, a%b)
c1, p1 = map(int, input().split())
c2, p2 = map(int, input().split())
a_p = p1 * p2
a_c = c1*p2 + c2*p1
Gcd = gcd(a_p, a_c)
a_p = a_p//Gcd
a_c = a_c//Gcd
print(a_c, a_p)
