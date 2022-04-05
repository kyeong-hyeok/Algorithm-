num = list(map(int, input()))
sumnum = num[0]
for i in range(1, len(num)):
    if sumnum <= 1 or num[i] <= 1:  # 0 혹은 1일 때 더하기
        sumnum += num[i]
    else:
        sumnum *= num[i]
print(sumnum)