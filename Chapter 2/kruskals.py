"""
A Python implemenation of Kruskals
"""


# Class to represent graph object
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary

    # function to add an edge to graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    # The main function to construct MST using Kruskal's
    # algorithm
    def kruskals_mst(self):

        result = []  # This will store the resultant MST

        i = 0  # An index variable, used for sorted edges
        e = 0  # An index variable, used for result[]

        # Step 1: Sort all the edges in non-decreasing
        # order of their
        # weight. If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = [];
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:

            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does't cause cycle,
            # include it in result and increment the index
            # of result for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge

        # print the contents of result[] to display the built MST
        print
        "Following are the edges in the constructed MST"
        for u, v, weight in result:
            # print str(u) + " -- " + str(v) + " == " + str(weight)
            print("%d -- %d == %d" % (u, v, weight))

        # Driver code


g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskals_mst()
