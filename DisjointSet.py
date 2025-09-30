""" A version that precomputes based on max length. """
class DisjointSet:
    def __init__(self, n):
        # n is the maximum number of elements - usually given in the problem spec
    
        # how deep element i is in the hierarchy
        self.rank = [0] * n
        # the parent of element i
        self.parent = list(range(n))

    def find(self, i):
        # search upwards in the tree
        if self.parent[i] != i:
            # path compression
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def same_set(self, x, y):
        # Same root? Same set.
        return self.find(x) == self.find(y)

    def union(self, x, y):
        # if same set, skip
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        
        # Place the lower rank set below the higher
        # If both are the same, the rank increases by 1
        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[yRoot] < self.rank[xRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1
            
            
""" A more flexible generic version. """
class DSU:
    def __init__(self):
        self.parent = []
        self.rank = []

    def add(self):  # adds a new singleton element
        i = len(self.parent)
        self.parent.append(i)
        self.rank.append(0)
        return i

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])  # path compression
        return self.parent[i]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[yRoot] < self.rank[xRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1