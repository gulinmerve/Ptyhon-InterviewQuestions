# rand5() fonksiyonu hazır kabul ediyoruz. Sonunun çözümünü fiziki olarak da görmek için aşağıdaki rand5() fonksiyonunu kullanabilirsiniz.
from random import randint
def rand5():
    return randint(1,5)

#
def rand7():
    a=rand5()+rand5()-1
    return a if a<8 else rand7()