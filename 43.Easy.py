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