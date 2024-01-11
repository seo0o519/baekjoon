n = int(input())
book_dict = {}
for _ in range(n):
    book = input()
    if book in book_dict:
        book_dict[book] += 1
    else:
        book_dict[book] = 1

best_seller = max(book_dict.values())  # 최댓값 찾기

selected_key = None

for key, value in book_dict.items():
    if value == best_seller:
        if selected_key is None or key < selected_key:
            selected_key = key

print(selected_key)
