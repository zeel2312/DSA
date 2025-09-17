def f(i,sum,arr,res):
    if(i == len(arr)): # base case
        res.append(sum)
        # print(res)
        return
    
    f(i+1,sum+arr[i],arr,res) #taking the element(picking)
    f(i+1,sum,arr,res) #not taking the element (not picking)
    # print(res1+res2)
    return sorted(res)

arr = [3,1,2]
print(f(0,0,arr,[]))