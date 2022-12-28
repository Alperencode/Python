class Ogrenci:
    count = 0

    def __init__(self,isim,soyad,numara):
        self.isim = isim
        self.soyad = soyad
        self.numara = numara
        self.email = isim+soyad+"@hotmail.com"
        Calisan.count += 1

    def GiveNameSurname(self):
        return self.isim+" "+self.soyad

ogrenci1 = Ogrenci("Alperen","Ağa",374)

print(ogrenci1.isim)
print("")
print(ogrenci1.email)

print(ogrenci1.GiveNameSurname())

print("")