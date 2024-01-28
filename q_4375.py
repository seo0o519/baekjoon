import sys
input =sys.stdin.readline

while True:
    try:
        n = int(input().rstrip())
    except:
        break
    num = '1'
    while True:
        if int(num) % n == 0:
            print(len(num))
            break
        else:
            num = num + '1'