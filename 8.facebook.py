# Çözüm-1
def check1(lst):
    count = 0
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            if count > 1:
                return False
            if i>1 and i<len(lst)-2 and lst[i-1] > lst[i+1] and lst[i] > lst[i+2]:
                return False    
            count += 1       
    return True


    # Çözüm-2
def check2(lst):
    count = 0
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            if i>1 and i<len(lst)-2 and lst[i-1] > lst[i+1] and lst[i] > lst[i+2]:
                return False    
            count += 1
    return bool(count<2) and True or False