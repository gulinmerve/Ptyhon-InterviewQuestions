#Solution1

def check_bishops(bishops, m):
    result = 0
    for i in range(len(bishops)):
        for j in range(len(bishops[i+1:])):
            result += abs(bishops[i+1+j][0] - bishops[i][0]) == abs(bishops[i+1+j][1] - bishops[i][1])
    return result
#
    def check_bishops2(bishops, m):
    return len([1 for i in range(len(bishops)) for j in range(len(bishops[i+1:])) if abs(bishops[i+1+j][0] - bishops[i][0]) == abs(bishops[i+1+j][1] - bishops[i][1])])


