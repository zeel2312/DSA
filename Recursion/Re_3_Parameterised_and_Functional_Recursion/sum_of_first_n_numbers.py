# #parameterized way
# def f(i,sum):
#     if (i<1): #base case
#         print(sum)
#         return
#     f(i-1,sum+i)
    
#functional way
def f(n):
    if(n == 0): #base case
        return 0
    return n + f(n-1) #returning the sum

n = 3
a = f(n) #f(n,0)
print(a)