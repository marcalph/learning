def f(i: int, values:list = []):
    values.append(i)
    print(values)
    return values

f(1)
f(2)
f(3)