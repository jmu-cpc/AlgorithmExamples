def bellman_ford(n, edges, start):
    """
    Bellman-Ford algorithm for graphs with possibly negative edges.
    Detects negative cycles reachable from the source.

    Parameters:
        n: number of nodes
        edges: list of (u, v, w) edges
        start: source vertex
    Returns:
        dist: shortest distances or -inf for nodes affected by negative cycles
        parent: predecessor list
    """
    INF = float('inf')
    dist = [INF] * n
    parent = [-1] * n
    dist[start] = 0

    # Relax edges n-1 times
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        if not updated:
            break

    # Detect negative cycles
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            dist[v] = -float('inf')  # or mark specially
            parent[v] = -1

    return dist, parent
