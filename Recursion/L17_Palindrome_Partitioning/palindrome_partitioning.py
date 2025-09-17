def f(index,s,ans,path):
    if(index == len(s)): #base case
        return ans.append(path[:]) #appending the path

    for i in range(index,len(s)):
        if(isPalindrome(s,index,i)): #checking for palindrome
            path.append(s[index:i+1])
            f(i+1,s,ans,path)
            path.pop() #backtracking
    
    return ans

def isPalindrome(s,start,end):
    return s[start:end+1] == s[start:end+1][::-1] #checking for palindrome if "ab == ba"

s = "aabb"
print(f(0,s,[],[]))