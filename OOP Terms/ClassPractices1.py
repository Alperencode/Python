# %%
class Calisan:

    count = 0

    def __init__(self,isim,zaman,maas):
        self.isim = isim
        self.zaman = zaman
        self.maas = maas
        Calisan.count = Calisan.count + 1 
    
    def NameTime(self):
        return self.isim + " " + self.zaman
    
Calisan1 = Calisan("Alperen","Freelance",5000)
Calisan2 = Calisan("Efe","Haftasonu",4000)
Calisan3 = Calisan("Umut","Haftaiçi",3500)
Calisan4 = Calisan("Egemen","Freelance",4500)

liste = [Calisan1,Calisan2,Calisan3,Calisan4]

for each in liste:
    if(each.maas>max_maas):
        max_maas = each.maas
        index = each

print(max_maas)

print(index.NameTime())
