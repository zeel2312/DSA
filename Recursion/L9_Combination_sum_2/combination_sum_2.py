def f(index,candidates,target,ans,res):
    candidates.sort()
    if(target == 0): #base case
        ans.append(res[:])
        return
    
    for i in range(index,len(candidates)):
        if(i>index and candidates[i] == candidates[i-1]): #skipping duplicates
            continue
        if(candidates[i] > target): #condition not satisfied as the array is sorted 
            break #we won't be able to find a smaller element to the right so we break
        
        res.append(candidates[i])
        f(i+1,candidates,target-candidates[i],ans,res) #taking the element
        res.pop() #backtracking
        
    return ans

candidates = [1,1,1,2,2]
target = 4
ans = []
print(f(0,candidates,target,ans,[]))