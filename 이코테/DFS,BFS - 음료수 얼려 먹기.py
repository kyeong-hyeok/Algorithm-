N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))


def dfs(x, y):  # 특정 노드 방문 후 연결된 모든 노드들도 방문
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if graph[x][y] == 0:  # 노드 방문하지 않았을 경우
        graph[x][y] = 1  # 노드 방문처리
        dfs(x - 1, y)  # 연결된 상하좌우 노드들 방문
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0  # 아이스크림 수
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1
print(result)
