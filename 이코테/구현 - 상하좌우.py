N = int(input())
move_list = list(input().split())
A = [1, 1]
for move in move_list:
    if move == "L" and A[1] > 1:  
        A[1] -= 1
    elif move == "R" and A[1] < N:
        A[1] += 1
    elif move == "U" and A[0] > 1:
        A[0] -= 1
    elif move == "D" and A[0] < N:
        A[0] += 1
print("%d %d" % (A[0], A[1]))
