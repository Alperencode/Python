#%%
class Birey:

    def __init__(self,isim:str,soyisim:str,tcno:int):
        self.isim = isim
        self.soyisim = soyisim
        self.tcno = tcno

class Calismayan(Birey): # Calismayan class'ı Birey class'ını inherit aldı
    pass                 # Yani Artık Birey class'ının bütün özellikleri bu class için geçerli

class Calisan(Birey):

    def __init__(self,isim:str,soyisim:str,tcno:int,idno:int,maas:int):
        Birey.__init__(self,isim,soyisim,tcno)   #Birey'in init'inde belirttiğimiz selfleri aldı
        self.idno = idno
        self.maas = maas

    def zam(self,deger:float):
        self.maas *= deger


class Muhendis(Calisan):
    """isim,soyisim,tcno,idno,maas,yazılım_dilleri,yabancı_diller,program"""
    def __init__(self,isim:str,soyisim:str,tcno:int,idno:int,maas:int,y_dilleri:tuple,yabanciDiller:tuple,bilinenProgramlar:tuple):
        Calisan.__init__(self,isim,soyisim,tcno,idno,maas)
        self.y_dilleri = y_dilleri
        self.yabanciDiller = yabanciDiller
        self.bilinenProgramlar = bilinenProgramlar

class Muhassebeci(Calisan):
    """isim,soyisim,tcno,idno,maas,program"""
    def __init__(self,isim:str,soyisim:str,tcno:int,idno:int,maas:int,bilinenProgramlar:tuple):
        Calisan.__init__(self,isim,soyisim,tcno,idno,maas)
        self.bilinenProgramlar = bilinenProgramlar

x = Muhendis("Alperen","Ağa",13456,1,8000,("Python","Php","Arduino"),("İngilizce",),("MC Office",))
y = Muhassebeci("Veli","Yılmaz",654321,2,5000,("CNR",))


print("X'in maaşı:",x.maas)
x.zam(1.8)
print("X'in maaşı:",x.maas)







#%%
