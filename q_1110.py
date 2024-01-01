start_num = input()
if len(start_num) < 2 :
    start_num = '0' + start_num
num = start_num
cycle = 0
while True:
    new_num = str(int(num[0]) + int(num[1]))
    if len(new_num) < 2:
        new_num = "0" + new_num

    num = num[1] + new_num[1]
    cycle += 1

    if num == start_num:
        break

    if len(num) < 2:
        num = "0" + num
print(cycle)


