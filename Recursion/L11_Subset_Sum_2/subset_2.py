def f(index,nums,ans,res):
    ans.append(res[:]) #base case
    for i in range(index, len(nums)):
        if (i != index) and (nums[i] == nums[i-1]): #skipping duplicates
            continue
        res.append(nums[i])
        f(i+1,nums,ans,res) #taking the element
        res.pop() #backtracking
    return ans
        
nums = [1,2,3]
ans = []
res = []
nums.sort() #to avoid duplicates
f(0,nums,ans,res)
print(ans)