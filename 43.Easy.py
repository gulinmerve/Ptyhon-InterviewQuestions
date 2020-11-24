def plusOne(digits):
    if digits[-1] != 9:
        digits[-1] += 1
    else:
        i=-1
        while -i <= len(digits) and (digits[i] == 9):
            digits[i] = 0
            i -= 1
        if i+1 == -len(digits):
            digits = [1] + digits
        else:
            digits[i] += 1
    return digits

# Çözüm-2
def plusOne2(digits):
    s = "".join([str(i) for i in digits])
    leftzeros = len(s) - len(str(int(s)))
    return [0]*leftzeros + [int(i) for i in str(int(s)+1)]

def addone(arr):
    num = int(''.join([str(i) for i in arr]))  # convert to int
    numback = num + 1 
    digits = [int(i) for i in str(numback)]  # convert to array
    return digits

def inc(digits):
    number=0
    for i in range (len(digits)):
        number+=digits[i]*(10**(len(digits)-1-i))
    a=[int(i) for i in (list(str(number+1)))]
    print (a)
