### Undirected graph Representation

# adjacency matrix
n = int(input()) # number of nodes in the graph input()
m = int(input()) # number of edges in the graph
adj = [[0 for i in range(n+1)] for j in range(n+1)] # adjacency list
for i in range(n+1):
    u = int(input()) # source node
    v = int(input()) # destination node
    adj[u][v] = 1
    adj[v][u] = 1
print(adj)

# adjacency list
n = int(input()) # number of nodes in the graph input()
m = int(input()) # number of edges in the graph
adj = [[] for i in range(n+1)] # adjacency list
for i in range(m):
    # u <---> v
    u = int(input()) # source node
    v = int(input()) # destination node
    adj[u].append(v)
    adj[v].append(u)
print(adj)

### Directed graph Representation

# adjacency list
n = int(input()) # number of nodes in the graph input()
m = int(input()) # number of edges in the graph
adj = [[] for i in range(n+1)] # adjacency list
for i in range(m):
    # u ---> v
    u = int(input()) # source node
    v = int(input()) # destination node
    adj[u].append(v)
print(adj)