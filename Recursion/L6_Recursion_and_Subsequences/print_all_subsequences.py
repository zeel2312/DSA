def f(i,arr,res):
    if(i >= len(arr)): #base case
        print(res)
        return
    res.append(arr[i])
    f(i+1,arr,res) #taking the element
    res.pop() #backtracking
    f(i+1,arr,res) #not taking the element
    

arr = [3,1,2]
print(f(0,arr,[]))
