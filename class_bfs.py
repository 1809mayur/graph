
class Graph:
    def __init__(self,n):
        self.adj = [[] for i in range(n+1)]
        self.visited = [0 for i in range(n+1)]
        self.que = []


    def add_edge(self,u,v):
        self.adj[u] += [v]
    
    def get_graph(self):
        return self.adj

    def bfs_traversal(self,src,path=[]):
        # assing the src into que.
        self.que.append(src)
        self.visited[src] = 1
        while self.que != []:
            val = self.que.pop(0)
            path.append(val)

            # check for adjancent node of val(node).
            for adj_node in self.adj[val]:
                if self.visited[adj_node] == 0:
                    self.que.append(adj_node)
                    self.visited[adj_node] = 1

        return path
        


def main():
    n,m = list(map(int,input().split()))

    # initialised graph.
    g = Graph(n)

    # adding element into undirected graph.
    for i in range(m):
        u,v = list(map(int,input().split()))
        g.add_edge(u,v)
        g.add_edge(v,u)

    # no component of graph should remain unvisited.
    for i in range(1,n+1):   # 1-based indexing.
        if g.visited[i] == 0:
            print(g.bfs_traversal(i))

    print(g.get_graph())


main()