N = int(input())
fear = list(map(int, input().split()))
fear.sort()
count = 0; group = 0
for i in fear:
    count += 1
    if i <= count & count != 1:   # 모험가의 수 >= 공포도  & 모험가 2명 이상
        group += 1
        count = 0
print(group)