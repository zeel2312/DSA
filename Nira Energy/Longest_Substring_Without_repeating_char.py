def lengthOfLongestSubstring(s):
    l = 0
    longestStr = set()
    res = 0
    for r in range(len(s)):
        while s[r] in longestStr: # shrink the window by 1 everytime we find a duplicate
            longestStr.remove(s[l])
            l += 1
        longestStr.add(s[r])
        res = max(res, r-l+1) # current window len -> r-l+1
    return res
    
 
s = "abcabcbb"
print(lengthOfLongestSubstring(s))