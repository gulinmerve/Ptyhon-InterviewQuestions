#https://edabit.com/challenge/b8wRDMWgMZTN2nmfx

def equal(a, b, c):
    listed = [a, b, c]
    repeat_list = [listed.count(i) for i in listed]
    if max(repeat_list) == 1:
        return 0
    else:
        return max(repeat_list)
print(equal(2, 4, 5))


def equal(a, b, c):
    if a==b==c: return 3
    elif a==b or b==c or a==c: return 2
    else: return 0
equal(2,4,5)

 def equal(a, b, c):
    	return [0,3,2,0][len(set([a,b,c]))]  
equal(3,3,6)
