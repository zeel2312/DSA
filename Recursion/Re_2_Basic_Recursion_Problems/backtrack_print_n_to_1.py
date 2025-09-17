def f(i,n):
    if (i>n): # base case
        return
    f(i+1,n)
    print(i)


n = 3
a = f(1,n)
print(a)