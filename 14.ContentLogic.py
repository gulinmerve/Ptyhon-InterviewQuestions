# Code for m/n:point_down:
def div(m,n):
    result=0
    while n<=m:
        m-=n
        result+=1
    return result