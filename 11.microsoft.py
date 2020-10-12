# Soruda read7() bize hazır olarak verildi diyor. Ancak read7() fiziki olarak elimizde olmadığı için programımızı test edemeyiz. Sorunun çözümünü fiziki olarak görülebilmesi maksadıyla aşağıdaki class ı ve read7() metodunu kullanabilirsiniz.



class Reader():
    def __init__(self, txt):
        self.index = 0
        self.txt = txt
    def read7(self):
        temp = self.txt[self.index:self.index+7]
        self.index += len(temp)
        return temp
myreader = Reader("Hello world")
print(myreader.read7())


# Class kafanızı karıştırıyorsa, aşağıdaki fonksiyonu kullanabilirsiniz.
text = "Hello world"
index = 0
def read7():
    global index
    temp = text[index:index+7]
    index += len(temp)
    return temp

#  class kullanarak çözüm
class fileread:
    def __init__(self):
        self.leftover = ""
    def readN(self, n):
        value = self.leftover
        text = None
        while len(value) < n and (text is None or len(text) == 7):
            text = read7()
            value += text
        self.leftover = value[n:]
        return value[:n]

# class kullanmadan çözüm
leftover = ""
def readN(n):
    global leftover
    value = leftover
    text = None
    while len(value) < n and (text is None or len(text) == 7):
        text = read7()
        value += text
    leftover = value[n:]
    return value[:n]