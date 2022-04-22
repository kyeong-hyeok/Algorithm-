from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])  # 큐 구현을 위해 deque 라이브러리 사용
    visited[start] = True  # 방문 처리
    while queue:  # 큐가 비어있지 않다면
        v = queue.popleft()  # 큐에서 상단 노드 꺼내기
        print(v, end=' ')
        for i in graph[v]:  # 꺼낸 큐와 인접한 노드들
            if not visited[i]:  # 방문하지 않은 노드들
                queue.append(i)  # 큐에 삽입
                visited[i] = True  # 방문 처리
