want = int(input())
stick_piece = [64]
while True:
    if sum(stick_piece)==want:
        break
    shortest = stick_piece.pop()
    stick_piece.append(shortest/2)
    if sum(stick_piece) < want:
        stick_piece.append(shortest/2)
print(len(stick_piece))