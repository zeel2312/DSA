def f(i, arr):
    n = len(arr)
    if(i >= n//2): #base case
        return True
    if(arr[i] != arr[n-i-1]):
        return False
    return f(i+1,arr) #recursive call

arr = "madam"
print(f(0,arr))