#%%
from datetime import date

# Date ve Datetime kullanımı
# print(date(2018,6,2)) # Yıl,Ay,Gün
# print(datetime(2018,6,2,18,30)) # Yıl,Ay,Gün,Saat,Dakika

class Kitap:
    def __init__(self,yazar:str,isim:str,basimTarihi:date,sayfaSayisi:int):
        self.yazar = yazar
        self.isim = isim
        self.basimTarihi = basimTarihi
        self.sayfaSayisi = sayfaSayisi

x = Kitap("Paulo Coelho", "Simyacı", date(2019,6,2), 184)

print(x.basimTarihi)



























#%%