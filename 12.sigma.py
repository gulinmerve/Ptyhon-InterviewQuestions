def rand5():
    x = rand7()
    return x if 1 <= x <= 5 else rand5()

#
def rand5():
    return int ((rand7()/7)*5)