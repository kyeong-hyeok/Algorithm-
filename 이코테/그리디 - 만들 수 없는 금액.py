N = int(input())
coin_list = list(map(int, input().split()))
coin_list.sort()
result = 1  # 만들 수 없는 최소 금액 1로 설정
for coin in coin_list:
    if result >= coin:  # 동전 값이 result 값 이하일 때 만들 수 있음
        result += coin  # 현재 동전 값을 더해 result 갱신
    else:
        break
print(result)
# 오름차순 정렬 -> 동전의 모든 조합 고려하여 접근, 시간 초과 -> 아이디어 참고.
