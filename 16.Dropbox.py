functions = []
for i in range(10):
    f = lambda j, i = i : i
    functions.append(f)
for f in functions:
    print(f(0)) 