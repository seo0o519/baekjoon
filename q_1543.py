txt = input()
word = input()
index = 0
cnt = 0
while index <= len(txt)-len(word):
    for i in range(len(word)):
        if txt[index+i] != word[i]:
            index += 1
            break
        if i==len(word)-1 and txt[index+i]==word[i]:
            cnt += 1
            index = index + i + 1
print(cnt)