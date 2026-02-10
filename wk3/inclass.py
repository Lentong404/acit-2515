def func(n):
    if n <= 0:
        result ="!\n"
    else:
        result = ("." * n) + "\n" + func(n-1)
    return result

print(func(3))