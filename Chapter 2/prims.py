"""
An implementation of Primm's Algorithm in Python using adjacency matrix
"""


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_mst(self, mst):
        print("Edge \t Weight")
        for i in range(1, self.vertices):
            print("{} - {} \t {}".format(mst[i], i, self.graph[i][mst[i]]))

    def min_key(self, key, mst_set):
        min = 100000000000000

        for vertex in range(self.vertices):
            if key[vertex] < min and not mst_set[vertex]:
                min = key[vertex]
                min_index = vertex
        return min_index

    def gen_mst(self):
        key = [100000000000000] * self.vertices  # Values used to pick minimum edge
        mst = [None] * self.vertices  # Stores constructed MST

        key[0] = 0  # Makes first key zero so it is the first one included
        mst_set = [False] * self.vertices  # Records vertices included in the MST
        mst[0] = -1  # This sets the first value to be the root of the MST so not included in calculations later
        for cout in range(self.vertices):

            # finds the minimum distance vertex not in MST
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.vertices):
                # Checks not the same node, not already included in MST and updates key value only in connector
                # and current value is greater than new distance and vertex not in MST
                if 0 < self.graph[u][v] < key[v] and not mst_set[v]:
                    key[v] = self.graph[u][v]
                    mst[v] = u

        return self.print_mst(mst)


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

g.gen_mst()
