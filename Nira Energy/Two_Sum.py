def twoSum(nums, target):
    dict_s = {} # dict to store values -> indices
    for i in range(len(nums)):
        x = nums[i]
        need = target - x
        
        if need in dict_s: # if value is already present in dict
            return [dict_s[need], i] # return both indices
        if x not in dict_s:
            dict_s[x] = i
    

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))