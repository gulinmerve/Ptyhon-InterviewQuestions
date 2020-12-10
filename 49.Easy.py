#Solution" added
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

def isHappy(n):
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum(int(i)**2 for i in str(n))        
    return True if n == 1 else False