def factorail_recurs(x):
    if x == 1:
        return 1
    else:
        return x*factorail_recurs(x-1)

print(factorail_recurs(6))