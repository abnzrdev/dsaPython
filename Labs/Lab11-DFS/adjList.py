# Create a way to create from input to the adjacency list and understand the code to describe
# so for now we have two things
# 1. From taking inputs we have to create adjacency list which basically means
# we are changing the graph in to something that we can use of

def addedge(adj, a, b):
    adj[a].append(b)
    adj[b].append(a)

if __name__ == "__main__":
    vertices = int(input("Vertices(Write the largest number in your vertices + 1)  : "))
    edge = int(input("Edges : "))
    adj = [[] for i in range(vertices)]

    for i in range(edge):
        u, v = map(int, input().split())
        addedge(adj, u, v)

    print(adj)

