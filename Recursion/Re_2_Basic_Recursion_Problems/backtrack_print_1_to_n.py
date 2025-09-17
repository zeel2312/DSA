def f(i,n):
    if (i<1): # base case
        return
    f(i-1,n)
    print(i)


n = 3
a = f(n,n)
print(a)