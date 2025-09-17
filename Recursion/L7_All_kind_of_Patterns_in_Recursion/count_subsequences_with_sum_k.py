def f(i,arr,sum,vsum):
    if(i == len(arr)): #base case
        if(vsum == sum):
            return 1
        return 0
    vsum += arr[i]
    l = f(i+1,arr,sum,vsum) #taking the element
    vsum -= arr[i]
    r = f(i+1,arr,sum,vsum) #not taking the element
    return l+r
    
arr = [1,2,1]
sum = 2
print(f(0,arr,sum,0))