def sol():
    student_num = int(input())
    student_id = [input() for _ in range(student_num)]
    id_len = len(student_id[0])
    lst = []
    ans = 0
    for i in range(1, id_len+1): # 단어 슬라이싱 개수
        for j in range(student_num): # 단어들
            if student_id[j][-i:] in lst:
                lst = []
                break
            else:
                lst.append(student_id[j][-i:])
                if j==(student_num-1):
                    ans = i
                    return ans
    return ans

print(sol())
