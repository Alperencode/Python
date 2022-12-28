from datetime import *
from random import randint

se = ["Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin",
"Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale",
"Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir",
"Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "Mersin", "İstanbul", "İzmir", 
"Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", 
"Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya",
"Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak",
"Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak",
"Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"]

class Sehir:
    def __init__(self,isim):
        self.__isim = isim
        self.__havaDurumu = ["Açık","Kapalı","Yağışlı","Sağanak Yağışlı"][random.randint(0, 3)]
        self.__sicaklik = random.randint(18,25)
    
    def getIsim(self):
        return self.__isim
    
    def  getSicaklik(self):
        return self.__sicaklik
    
    def getHavaDurumu(self):
        return self.__havaDurumu

    def setIsim(self,yenisim):
        self.__isim = yenisim

    def setSicaklik(self,yenisicaklik):
        self.__sicaklik = yenisicaklik
    
    def setHavaDurumu(self,durum):
        if durum not in ["Açık","Kapalı","Yağışlı","Sağanak Yağışlı"]:
            return "Lütfen geçerli bir hava durumu giriniz."
        else:
            self.__havaDurumu = durum
        
    def __str__(self):
        return "İsim: " + self.__isim + " Sıcaklık: " + str(self.__sicaklik) + " Hava Durumu: " + self.__havaDurumu

class Ucus:
    def __init__(self,nereden:Sehir,nereye:Sehir,tarih:datetime):
        self.__nereden = nereden
        self.__nereye = nereye
        self.__tarih = tarih

    def rotar(self,addTime):
        day = self.__tarih.day
        hour = self.__tarih.hour
        minute = self.__tarih.minute
        if (minute + Addtime) >= 60:
            hour += int((minute + Addtime) / 60)
            minute = (minute + Addtime) % 60
            
            if hour >= 24:
                day += int(hour / 24)
                hour = hour % 24 

        newDate = datetime(self.__tarih.year,self.__tarih.month,day,hour,minute)
        self.__tarih = newDate

    def getTarih(self):
        return self.__tarih
        