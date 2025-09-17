def f(ind,nums,ans):
   if(ind == len(nums)): #base case
       return ans.append(nums[:])
   
   for i in range(ind,len(nums)):
       nums[ind],nums[i] = nums[i],nums[ind] #swapping #swap(nums[index],nums[i])
       f(ind+1,nums,ans) #recursive call
       nums[ind],nums[i] = nums[i],nums[ind] #backtracking #swap(nums[index],nums[i])
   return ans
    
    
nums = [1,2,3]
ans = []
print(f(0,nums,ans))