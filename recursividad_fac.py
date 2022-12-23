def factorial_normal(x):
    a=1
    i=2
    while i<=x:
        a *= i 
        i += 1
    return a

print(factorial_normal(5))