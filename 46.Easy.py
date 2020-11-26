def reply(input):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    num = list(range(1,27))
    data = dict(zip(num, letters))
    if input < 27 :
        return data[input]
    else:
        first = data[input // len(letters)]
        second = data[input % len(letters)]
        return first+second

def convertToTitle(n):
    result = ""
    while n > 26:
        result = chr(65+(n-1)%26)  + result  
        n = (n-1) // 26
    return chr(64+n) + result  
