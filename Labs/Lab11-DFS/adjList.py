# Create a way to create from input to the adjacency list and understand the code to describe
# so for now we have two things
# 1. From taking inputs we have to create adjacency list which basically means
# we are changing the graph in to something that we can use of

def addedge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
    edge = int(input())
    adj = [[] for i in range(edge)]
    for _ in range(edge):
        u, v = map(int, input().split())
        addedge(adj, u, v)

    print(adj)
