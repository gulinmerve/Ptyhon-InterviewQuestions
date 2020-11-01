# rand5() fonksiyonu hazır kabul ediyoruz. Sonunun çözümünü fiziki olarak da görmek için aşağıdaki rand5() fonksiyonunu kullanabilirsiniz.
from random import randint
def rand5():
    return randint(1,5)


d={}
for i in range(700000):
  # a = (5*(rand5()-1) + rand5() - 1 )%7+1  
  a=(rand5() + rand5() + rand5()+ rand5()+ rand5()+ rand5())%7+1
  if a in d: d[a]+=1
  else: d[a]=1
x=dict(sorted(d.items(),key=lambda x:x[0]))
df3=pd.DataFrame.from_dict(x, orient="index")
df3.plot(kind='bar');