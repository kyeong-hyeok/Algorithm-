S = list(map(int, input()))
count = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:  # 불연속 지점 개수 찾기
        count += 1
if count % 2 != 0:
    count += 1
print(count//2)
