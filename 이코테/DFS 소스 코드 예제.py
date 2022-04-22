def dfs(graph, v, visited):
    visited[v] = True  # 현재 노드 방문 처리
    print(v, end=' ')
    for i in graph[v]:  # 현재 노드와 연결된 노드 방문
        if not visited[i]:  # 방문하지 않은 노드들에 대해 재귀적으로 dfs 수행
            dfs(graph, i, visited)
