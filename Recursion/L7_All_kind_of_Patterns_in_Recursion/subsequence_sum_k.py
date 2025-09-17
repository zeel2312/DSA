def f(i,arr,sum,res,vsum):
    if(i == len(arr)): #base case
        if(vsum == sum):
            print(res)
        return
    res.append(arr[i])
    vsum += arr[i]
    f(i+1,arr,sum,res,vsum) #taking the element
    res.pop() #backtracking
    vsum -= arr[i]
    f(i+1,arr,sum,res,vsum) #not taking the element
    
arr = [1,2,1]
sum = 2
res = []
f(0,arr,sum,res,0)