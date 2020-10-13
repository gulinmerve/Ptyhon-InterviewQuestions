def checkform(text):
    total = [0,0]
    for i in text:
        if i == '(' :
            total[0] += 1
        elif i == ')' and total[0] > 0:
            total[0] -= 1
        else:
            total[1] += 1
    return sum(total)