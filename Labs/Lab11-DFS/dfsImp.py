# for dfs implementation we need source
# then we just have to include our implementaion of adjList after adding them impl
# We can traverse through the source if it exist

def addedge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def dfs(adj, source, visited, traversal):
    visited[source] = True
    traversal.append(source)

    for neigh in adj[source]:
        if not visited[neigh]:
            dfs(adj, neigh, visited, traversal)


if __name__ == "__main__":
    vertices = int(input("Vertices: "))
    edges = int(input("Edges: "))
    adj = [[] for _ in range(edges)]

    for _ in range(edges):
        u, v = map(int, input().split())
        addedge(adj, u, v)

    source = int(input("Source: "))
    visited = [False] * edges
    traversal = []

    dfs(adj, source, visited, traversal)
    print(traversal)




