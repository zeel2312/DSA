def f(i,arr,sum,res,vsum):
    if(i == len(arr)): #base case
        if(vsum == sum): #condition satisfied
            print(res)
            return True
        return False #condition not satisfied
    
    res.append(arr[i])
    vsum += arr[i]
    
    if f(i+1,arr,sum,res,vsum) == True: #taking the element
        return True
    
    res.pop() #backtracking
    vsum -= arr[i]
    
    if f(i+1,arr,sum,res,vsum) == True: #not taking the element
        return True
    
    return False
    
arr = [1,2,1]
sum = 2
res = []
f(0,arr,sum,res,0)