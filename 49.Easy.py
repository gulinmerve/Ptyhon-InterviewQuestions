def happy(n):
    answer=[]
    while n!=1:
        summ=0
        for i in str(n):
            summ+=int(i)**2
        if summ in answer: 
            return False
        else:
            answer.append(summ)
        n=summ
    return True