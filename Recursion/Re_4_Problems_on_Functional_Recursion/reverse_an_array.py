# def f(l,r,arr):
#     if(l >= r): #base case
#         return
#     temp = arr[l] #swapping
#     arr[l] = arr[r]
#     arr[r] = temp
#     f(l+1,r-1,arr) #recursive call
    
#using single pointer
def f(i, arr):
    n = len(arr)
    if(i >= n//2): #base case
        return
    temp = arr[i]
    arr[i] = arr[n-i-1]
    arr[n-i-1] = temp
    f(i+1,arr)
    
arr = [1,2,3,4,5]
f(0,arr) #f(0,4,arr)
print(arr)