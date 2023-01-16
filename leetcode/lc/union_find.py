class UnionFind:
    def __init__(self):
        self._ds = {}

    def find(self, x):
        ds = self._ds
        if x != ds.setdefault(x, x):
            ds[x] = self.find(ds[x])
        return ds[x]

    def union(self, x, y):
        self._ds[self.find(x)] = self.find(y)

    def __contains__(self, a):
        return a in self._ds
