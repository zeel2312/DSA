def findOrder(k, n, al_dict):
    adj = [[] for i in range(k)]
    
    for i in range(n-1):
        s1 = al_dict[i] # s1 = "baa", s2 = "abcd"
        s2 = al_dict[i+1]
        length = min(len(s1), len(s2))
        
        for ptr in range(length): # loop though each character
            if s1[ptr] != s2[ptr]: # if they are not equal
                # directed edge from s1 -> s2, - 'a' to store the value in terms of 0,1,2...
                adj[ord(s1[ptr]) - ord('a')].append(ord(s2[ptr]) - ord('a')) 
                break
        
    topo = topoSort(k, adj)
    ans = ""
    for i in topo:
        ans += chr(i + ord('a')) # converting 0,1,2... to 'a','b','c'
    return ans
        
def topoSort(V, adjList):
    indegree = [0 for i in range(V)]
    for i in range(V): # calculate indegree
        for j in adjList[i]: # for each adjacent node
            indegree[j] += 1 
    
    queue = []
    for i in range(V): # push all nodes with 0 indegree to the queue
        if indegree[i] == 0:
            queue.append(i)
    
    topo = [] # topological sort
    while queue:
        node = queue.pop(0) # pop from the queue
        topo.append(node) # add to topological sort
        # node is in your topo sort
        for i in adjList[node]:
            indegree[i] -= 1 # so please decrease its neighbours count form your indegree
            if indegree[i] == 0: # if the neighbour count is 0
                queue.append(i) # push to the queue
    return topo

# Time Complexity: 
# Space Complexity: 

K = 4 # alphabets from english dictonary [a,b,c,d]
N = 5 # length of alien dictonary
al_dict = ["baa", "abcd", "abca", "cab", "cad"]
print(findOrder(K, N, al_dict))
