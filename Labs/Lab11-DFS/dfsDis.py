# DFS for disconnected graph
# for this one we are doing for disconnected graphs

def addedge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def dfsrec(adj, source, visited):
    visited[source] = True
    print(source, end = " ")
    for neigh in adj[source]:
        if not visited[neigh]:
            dfsrec(adj, neigh, visited)

def dfs(adj, source):
    visited = [False] * len(adj)
    dfsrec(adj, source, visited)

    for u in range(len(adj)):
        if not visited[u] and len(adj[u]) > 0:
            dfsrec(adj, u, visited)

if __name__ == "__main__":

    edge = int(input())
    vertex = int(input())
    adj = [[] for i in range(vertex)]

    for i in range(edge):
        u, v = map(int, input().split())
        addedge(adj, u, v)

    source = int(input("source : "))
    dfs(adj,source)
