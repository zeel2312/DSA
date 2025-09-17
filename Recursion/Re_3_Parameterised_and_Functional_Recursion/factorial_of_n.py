# def f(n):
#     if(n == 0): #base case
#         return 1
#     return n * f(n-1) #returning the product

# Parameterized way
def f(i,prod):
    if (i<1): #base case
        print(prod)
        return
    f(i-1,prod*i)

n = 5
a = f(n,1)
# print(a)