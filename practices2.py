class Insan:
    def __init__(self,isim:str,soyisim:str,yas:int):
        self.__isim = isim
        self.__soyisim = soyisim
        self.__yas = yas

    def getIsim(self):
        return self.__isim

    def getSoyisim(self):
        return self.__soyisim
    
    def getYas(self):
        return str(self.__yas)

    def changeIsim(self,isim:str):
        if(type(isim) == "str"):
            self.__isim = isim
        else:
            return "Please try with strings"
    
    def changeSoyisim(self,soyisim:str):
        if(type(soyisim) == "str"):
            self.__soyisim = soyisim
        else:
            return "Please try with strings"

    def changeYas(self,yas:int):
        if(type(yas) == "int"):
            self.__yas = yas
        else:
            return "Please try with integers"

    def __str__(self):
        return "İsim: " + self.__isim + " Soyisim: " + self.__soyisim + " Yaş: " + self.__yas
    
    def __len__(self):
        return self.__yas
    
    def __del__(self):
        print("{} {} isimli kişi silindi! ".format(self.__isim, self.__soyisim))

class Calismayan(Insan):
    pass

class Calisan(Insan):
    def __init__(self,isim:str,soyisim:str,yas:int,isi:str,bilinen_diller:tuple):
        Insan.__init__(self,isim,soyisim,yas)
        self.__isim = isim    
        self.__isi = isi
        self.__bilinen_diller = bilinen_diller

    def getIs(self):
        return self.__isi

    def getDiller(self):
        return self.__bilinen_diller

    def changeIs(self,yenis:str):
        if(type(yenis) == "str"):
            self.__isi = yenis
        else:
            return "Please try with strings"

    def changeDiller(self,diller:tuple):
        if(type(diller) == "tuple"):
            self.__bilinen_diller = diller
        else:
            return "Please try with tuples"

    def addDil(self,*args):
        if(type(args) == tuple):
            for x in args:
                self.__bilinen_diller += x  
        else:
            return "Please try with tuples"      

    def __str__(self):
        return self.__isim + " İsimli kişi " + self.__isi + " işinde çalışıyor."

    def __del__(self):
        print(self.__isi,"işinde çalışan",self.__isim,"isimli kişi silindi!")

x = Calisan("Alperen","Ağa",17,"Freelance Developer",("Python","Php","Arduino"))
y = Calisan("Alperen","Ağa",17,"Freelance Developer",("Python","Php","Arduino"))

