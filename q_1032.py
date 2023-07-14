num = int(input())
file_name = [0] * num
for i in range(num):
    file_name[i] = input()

file_name_len = len(file_name[0])
ans = ""
for i in range(1,num):
    for j in range(file_name_len):
        if file_name[0][j]==file_name[i][j]:
            ans = ans + file_name[0][j]
        else : ans = ans + "?"
    file_name[0] = ans[:]
    ans=""
print(file_name[0])