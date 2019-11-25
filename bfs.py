from collections import defaultdict
from functools import reduce
from itertools import count


class Graph(object):
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(set)

    def connect(self, i, j):
        self.edges[i].add(j)
        self.edges[j].add(i)

    def find_all_distances(self, s):
        visited = set()
        current = set([s])
        distance = [-1] * self.n

        for step in count():
            for e in current:
                distance[e] = 6 * step

            current = reduce(set.union, [self.edges[e] for e in current], set()).difference(visited)
            visited.update(current)

            if not current:
                break

        distance[s:s+1] = []
        return distance


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n,m = [int(value) for value in input().split()]
        graph = Graph(n)
        for i in range(m):
            x,y = [int(x) for x in input().split()]
            graph.connect(x-1,y-1)
        s = int(input())
        print(*graph.find_all_distances(s-1))

