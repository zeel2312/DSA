from collections import deque

def minimumMultiplications(arr, start, end):
    mod = 100000
    q = deque()
    q.append((0, start)) # (steps, number)
    dist = [float('inf')] * (100000)
    dist[start] = 0

    while q:
        steps, number = q.popleft()
        print(steps, number)
        for i in arr:
            NewNum = (i * number) % mod
            print("multiplication: ", NewNum)
            if steps+1 < dist[NewNum]:
                dist[NewNum] = steps+1
                if NewNum == end:
                    print(NewNum)
                    return steps + 1
                q.append((steps+1, NewNum))
                
    return -1
    
# Time: O(N)
# Space: O(N)
    
arr = [2,5,7]
start = 3
end = 75
print(minimumMultiplications(arr, start, end))
