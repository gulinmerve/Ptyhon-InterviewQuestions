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