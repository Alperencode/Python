# %%
class Calisan:

    zam_orani = 2.5     # Class'ın içindeki variable'ımız
    count = 0

    def __init__(self,isim,zaman,maas):
        self.isim = isim
        self.zaman = zaman
        self.maas = maas
        Calisan.count = Calisan.count + 1  

    def zam_yap(self):
        self.maas = self.maas + self.maas*self.zam_orani

Calisan1 = Calisan("Alperen","Freelance",5000)
Calisan2 = Calisan("Ahmet","Haftaici",5000)
Calisan3 = Calisan("Umut","Haftasonu",5000)
Calisan4 = Calisan("Efe","Freelance",5000)

print(Calisan1.maas)
print("")
Calisan1.zam_yap()
print(Calisan1.maas)

print("")

Calisan.count  #sayaç
