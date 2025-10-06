from collections import defaultdict # needed for all path reconstruction
import heapq # needed for dijkstra

def dijkstra(n, adj, start):
    """
    Dijkstra's algorithm for shortest paths from a single source.
    Works only with non-negative edge weights.

    Parameters:
        n: number of nodes (0-indexed)
        adj: adjacency list -> adj[u] = [(v, w), ...]
        start: source vertex
    Returns:
        dist: list of shortest distances
        parent: list for path reconstruction
    """
    dist = [float("inf")] * n
    dist[start] = 0 # Distance from start->start is of course 0
    pq = [(0, start)] # Python heapq uses a list unde the hood as a min-heap
    parents = [-1] * n # used for path reconstruction

    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue # Skip nodes we have visited - we did so optimally
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parents[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, parents

def reconstruct_shortest_path(parents, start, target):
    """Reconstruct the shortest path.
    
    NOTE: this is O(n). If you want to reconstruct all paths, it can be done more optimally
    by doing all path reconstructions simultaneously using similar logic to that of below.

    Args:
        parents (int[]): a mapping of a shortest path where parents[i] = one step closer 
            to the start from vertex_i
        start (int): the starting node of the path
        target (int): _description_

    Returns:
        int[]: a path from start -> target (or None if no path exists)
    """
    path = []
    while parents[target] != -1:
        path.append(target)
        target = parents[target]
    if path[-1] != start:
        path = None # Unreachable target. Implies the graph is disconnected
    else:
        path.reverse()
    return path


def reconstruct_shortest_path(parents, start, target):
    """Reconstruct the shortest path from 'start' to 'target' using a parent map.

    NOTE: O(V). For reconstructing all paths simultaneously, use a BFS-like approach. When
        doing multiple lookups, caching paths is a useful speedup.

    Args:
        parents (list[int]): parent[v] = predecessor of v on the shortest path
        start (int): source vertex
        target (int): destination vertex

    Returns:
        list[int]: path from start -> target (inclusive), or None if unreachable
    """
    path = []
    cur = target
    while cur != -1:
        path.append(cur)
        if cur == start:
            break
        cur = parents[cur]
    else:
        # loop ended without finding start. Implies target is 
        # unreachable because the graph is disconnected
        return None

    path.reverse()
    return path


def reconstruct_all_shortest_paths(parents, start):
    """Reconstruct shortest paths from 'start' to every reachable node.

    NOTE: This runs in O(V) and reuses parent relationships directly,
    avoiding repeated reverse traversals for each target.

    Args:
        parents (list[int]): parent[v] = predecessor of v on the shortest path
        start (int): source vertex

    Returns:
        dict[int, list[int]]: mapping node -> path from start -> node
    """
    paths = defaultdict(list)

    for v in range(len(parents)):
        if v == start:
            paths[v] = [start]
            continue

        # Follow parent chain backwards
        path = []
        cur = v
        while cur != -1:
            path.append(cur)
            if cur == start:
                break
            cur = parents[cur]
        else:
            # Unreachable node
            continue

        path.reverse()
        paths[v] = path

    return dict(paths)