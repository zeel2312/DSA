def f(n):
    if(n<=1): #base case
        return n
    last = f(n-1)
    second_last = f(n-2)
    return last + second_last

n = 4
print(f(n))