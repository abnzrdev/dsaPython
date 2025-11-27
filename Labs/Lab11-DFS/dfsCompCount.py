# Trying to find the number of component that a graph has

def addedge(adj, a, b):
    adj[a].append(b)
    adj[b].append(a)

def dfsrec(adj, source, visited):
    visited[source] = True
    for neigh in adj[source]:
        if not visited[neigh]:
            dfsrec(adj, neigh, visited)

def dfs(adj):
    visited = [False] * len(adj)
    comp = 0
    for u in range(len(adj)):
        if not visited[u]:
            comp += 1
            dfsrec(adj, u, visited)

    return comp

if __name__ == "__main__":
    edge = int(input())
    vertex = int(input())
    adj = [[] for i in range(vertex)]

    for i in range(edge):
        u, v = map(int, input().split())
        addedge(adj, u, v)

    count = dfs(adj)
    print(count)