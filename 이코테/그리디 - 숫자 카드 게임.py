import sys
N, M = map(int, sys.stdin.readline().split())
maxcard = 0
for i in range(N):
    card_list = list(map(int, sys.stdin.readline().split()))
    num = min(card_list)
    if num > maxcard:
        maxcard = num
print(maxcard)