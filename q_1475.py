room_number = input()
lst = [0,0,0,0,0,0,0,0,0,0]
for i in room_number:
    lst[int(i)] += 1

if max(lst) == lst[6] or max(lst) == lst[9]:
    if lst[6] > lst[9]:
        while lst[6] > lst[9]:
            lst[6] -= 1
            lst[9] += 1
    elif lst[9] > lst[6]:
        while lst[9] > lst[6]:
            lst[9] -= 1
            lst[6] += 1
    
print(max(lst))
