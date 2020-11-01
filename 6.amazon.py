#Çözüm1
def staircase(n, X):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return sum(staircase(n - x, X) for x in X)