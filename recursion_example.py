def calculate (x):
    if x % 2 == 0 or x < 2:
        return x
    else:
        x = x%2
        calculate (x)

print(calculate (10))
print(calculate (9))
