S = list(input())
S.sort()
count = 0
for i in range(len(S)):
    if 'A' <= S[i] <= 'Z':  # S[i]가 알파벳일 때
        p = i
        break
    else:  # S[i]가 숫자일 때
        count += int(S[i])
S.append(str(count))  # 리스트 뒤에 count 값 삽입
S = ''.join(S)  # 리스트를 문자열로 변환
print(S[p:])
