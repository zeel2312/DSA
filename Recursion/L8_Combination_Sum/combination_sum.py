def f(i,candidates,target,ans,res):
    if(i == len(candidates)): #base case
        if(target == 0): 
            ans.append(res[:])
        return
    
    if(candidates[i] <= target): #taking the element
        res.append(candidates[i])
        f(i,candidates,target-candidates[i],ans,res)
        res.pop() #backtracking
        
    f(i+1,candidates,target,ans,res) #not taking the element

    return ans

candidates = [2,3,6,7]
target = 7
ans = []
print(f(0,candidates,target,ans,[]))