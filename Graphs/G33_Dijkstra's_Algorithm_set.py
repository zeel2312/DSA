def dijkstra(V, adj, S):
    st = set()
    dist = [float('inf')] * V
    dist[S] = 0
    st.add((0,S))
    
    while st:
        dis, node = min(st) # this is a O(n) operation
        st.remove((dis,node))
        
        for adjNode, edgeWeight in adj[node]:
            if dis + edgeWeight < dist[adjNode]:
                # erase old pair if existed
                if dist[adjNode] != float('inf'):
                    st.discard((dist[adjNode], adjNode))
                # update with better distance
                dist[adjNode] = dis + edgeWeight
                st.add((dist[adjNode], adjNode))
    return dist
    
# Time Complexity: O(V^2)
# Space Complexity: O(V)
     
# Test Case
V = 6 # 0-5 nodes
adj = [
    [(1, 4), (2, 2)],       # 0
    [(2, 5), (3, 10)],      # 1
    [(4, 3)],               # 2
    [(5, 11)],              # 3
    [(3, 4)],               # 4
    []                      # 5
]
S = 0 # source
print(dijkstra(V, adj, S))