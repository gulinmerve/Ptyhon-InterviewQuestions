#https://edabit.com/challenge/NZwFY7HyeBTM25guM

def convert_to_decimal(perc):
    new_list = []
    for i in perc:
        perc = i.replace("%", "")
        new_list.append(float(perc)*0.01)
    return new_list
print(convert_to_decimal(["1%", "2%", "3%"]))