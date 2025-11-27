def addedge(adj, a, b):
    adj[a].append(b)
    adj[b].append(a)


def dfs(adj, source, visited=None):
    if visited == None:
        visited = [False] * len(adj)

    visited[source] = True
    print(source, end=" ")

    for neigh in adj[source]:
        if not visited[neigh]:
            dfs(adj, neigh, visited)


if __name__ == "__main__":
    vertices = int(input("Vertices(Write the largest number in your vertices + 1)  : "))
    edge = int(input("Edges : "))
    adj = [[] for i in range(vertices)]

    for i in range(edge):
        u, v = map(int, input().split())
        addedge(adj, u, v)

    print(adj)

    source = int(input("source : "))
    dfs(adj, source)


