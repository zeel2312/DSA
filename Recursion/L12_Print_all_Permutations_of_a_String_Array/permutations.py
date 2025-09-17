def f(nums,res,map,ans):
    if(len(map) == len(nums)): #base case
        ans.append(res[:])
        return
    
    for i in range(len(nums)):
        if(i in map): #skipping duplicates
            continue
        res.append(nums[i]) #adding element
        map[i] = 1 #marking visited
        # print("Before: ", map)
        f(nums,res,map,ans)
        map.pop(i) #backtracking
        # print("After: ", map)
        res.pop() #backtracking
    return ans
    
    
nums = [1,2,3]
res = []
map = {}
ans = []
print(f(nums,res,map,ans))
