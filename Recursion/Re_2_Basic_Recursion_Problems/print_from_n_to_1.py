def f(i,n):
    if (i<1): # base case
        return
    print(i)
    f(i-1,n) # because we have to go backwards


n = 3
a = f(n,n)
print(a)