from collections import deque

def zero_one_bfs(n, adj, start):
    """
    0-1 BFS for graphs with edge weights of 0 or 1.
    Uses deque instead of a heap for O(V + E) complexity.
    """
    INF = float('inf')
    dist = [INF] * n
    parent = [-1] * n
    dist[start] = 0
    dq = deque([start])

    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                if w == 0:
                    dq.appendleft(v)  # zero-weight → higher priority
                else:
                    dq.append(v)

    return dist, parent
