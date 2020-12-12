#https://edabit.com/challenge/b8wRDMWgMZTN2nmfx

def equal(a, b, c):
    listed = [a, b, c]
    repeat_list = [listed.count(i) for i in listed]
    if max(repeat_list) == 1:
        return 0
    else:
        return max(repeat_list)
print(equal(2, 4, 5))
