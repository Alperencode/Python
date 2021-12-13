# ========= Modules =========
from datetime import datetime
import random

# ========= All Classes =========
class Sehir:
    def __init__(self,isim):
        self.__isim = isim
        self.__sicaklik = random.randint(18, 25)
        self.__havaDurumu = ["Açık","Kapalı","Yağışlı","Sağanak Yağışlı"][random.randint(0,3)]

    def getIsim(self):
        return self.__isim

    def getSicaklik(self):
        return self.__sicaklik

    def getHavaDurumu(self):
        return self.__havaDurumu

    def setSicaklik(self,sicaklik:int):
        self.__sicaklik = sicaklik

    def setHavaDurumu(self,durum):
        if durum not in ["Açık","Kapalı","Yağışlı","Sağanak Yağışlı"]:
            return "Lütfen geçerli bir durum ile tekrar deneyiniz."
        else:
            self.__havaDurumu = durum

    def __str__(self):
        return self.__isim
        
class Ucus:

    def __init__(self,bulundugu:Sehir,gidilecek:Sehir,tarih:datetime):
        self.__bulundugu = bulundugu
        self.__gidilecek = gidilecek
        self.__tarih = tarih

    def rotar(self,Addtime):
        day = self.__tarih.day
        hour = self.__tarih.hour
        minute = self.__tarih.minute

        if (minute + Addtime) >= 60: # Eğer tarihteki süre ve eklenen süre 60'ı geçerse
            hour += int((minute + Addtime) / 60) # Saat 4 += (50 + 30) -> 80/60 -> int(1,x) -> 1               
            minute = (minute + Addtime) % 60  # Dakika ise direk setleniyor -> (50+30) -> 80 / 60'dan kalan yeni dakika oluyor   
            if hour >= 24: # Eğer saat 24'ü geçerse gün de setlenicek demek
                day += int(hour / 24)  # gün += saat'in 24 ile bölümü -> genellikle 1
                hour = hour % 24 # eski saat 0 = 0 % 24 -> 1 -> hour = 1

        newDate = datetime(self.__tarih.year,self.__tarih.month,day,hour,minute) # Yeni tarihlerin hepsi bir datetime değişkenine atanıyor
        self.__tarih = newDate # datetime değişkeni de self.__tarih'e atanıyor dolayısıyla tarih yenilenmiş oluyor
    
    def getBulundugu(self):
        return self.__bulundugu

    def getGidilecek(self):
        return self.__gidilecek

    def getTarih(self):
        return self.__tarih

class Yolcu:
    def __init__(self,isim,soyisim,tc):
        self.__isim = isim
        self.__soyisim = soyisim
        self.__tc = tc
    
    def getIsim(self):
        return self.__isim

    def getSoyisim(self):
        return self.__soyisim

    def getTc(self):
        return self.__tc

class Bilet:
    def __init__(self, yolcu:Yolcu,ucus:Ucus,koltukNumarası:int):
        self.__yolcu = yolcu
        self.__ucus = ucus
        self.__koltukNo = koltukNumarası
    
    def __str__(self):
        string = """
        İsim          : {}
        Soyisim       : {}
        T.C.          : {}
        Uçuş Tarihi   : {}
        Uçus Saati    : {}
        Bulunduğu Yer : {}
        Gidilecek Yer : {}   ---   Hava Durumu: {}
        Koltuk No     : {}
        """.format(self.__yolcu.getIsim(),self.__yolcu.getSoyisim(),self.__yolcu.getTc(),self.__ucus.getTarih().date(),self.__ucus.getTarih().time(),self.__ucus.getBulundugu(),self.__ucus.getGidilecek(),self.__ucus.getGidilecek().getHavaDurumu(),self.__koltukNo)
        return string
    
    def getUcus(self):
        return self.__ucus

    def getIsim(self):
        return self.__yolcu.getIsim()
    
    def getSoyisim(self): 
        return self.__yolcu.getSoyisim()

    def getTc(self):
        return self.__yolcu.getTc()
    
    def getUcusTarihi(self):
        print(self.__ucus.getTarih().date())
    
    def getUcusSaati(self):
        print(self.__ucus.getTarih().time())
    
class Pegasus:
    
    def __init__(self):

        # ========= Listeler =========
        self.__aktifBiletler = list()  
        self.__gecmisBiletler = list()
        self.__aktifUcuslar = list()
        self.__gecmisUcuslar = list()
        # ========= Listelerin Amacı =========
        # Class'ın metodlarını kullanarak, kayıt tutmak için ileride listelere eleman ekleyip silicez

    def BiletAl(self,yolcu:Yolcu,ucus:Ucus,koltukNumarasi):
        # ========= Bilet Class'ı =========
        if ucus in self.__aktifUcuslar:
            bilet = Bilet(yolcu,ucus,koltukNumarasi)
            self.__aktifBiletler.append(bilet)
            return bilet
        # Bilet class'ını kullanarak aktif biletlere bilet ekliyoruz

    def UcusOlustur(self,bulundugu:Sehir,gidilecek:Sehir,tarih:datetime):
        ucus = Ucus(bulundugu,gidilecek,tarih)
        self.__aktifUcuslar.append(ucus)
        return ucus
        # Ucus class'ını kullanarak aktif uçuşlara uçuş ekliyoruz

    def BiletIptal(self,bilet:Bilet):
        if bilet in self.__aktifBiletler:
            self.__aktifBiletler.remove(bilet)
            print("Success: Bilet iptal edildi!") 
            # Geçmiş biletlere bilet eklenmiyor çünkü bilet silme işlemi yapılmıyor iptal işlemi yapılıyor
        else:
            print("Error: Böyle bir bilet bulunamadı...")

    def UcusGerceklesti(self,ucus:Ucus):
        
        # ========= For Döngüsü =========
        for bilet in self.__aktifBiletler: # Bilet adındaki değişken aktif biletleri geziyor
            if bilet.getUcus() == ucus:    # Eğer biletin uçuşu girilen değer uçusa eşit ise
                self.__aktifBiletler.remove(bilet)  # O bilet aktif biletlerden siliniyor
                self.__gecmisBiletler.append(bilet) # Ve geçmiş biletlere ekleniyor
        
        # ========= Döngü Dışında =========
        self.__aktifUcuslar.remove(ucus)  # Girilen uçuş aktif uçuşlardan siliniyor
        self.__gecmisUcuslar.append(ucus) # Ve geçmiş uçuşlara ekleniyor

    def rotar(self,ucus:Ucus,dakika):
        ucus.rotar(dakika)

# ========= Creating 'Bilet' - 1 =========
# bilet1 = Bilet(Yolcu("Zeynep","Ağa",654321),Ucus(Sehir("İstanbul"),Sehir("Ankara"),datetime(2019,6,10,7,00)),"A3")
# print(bilet1)
# Bilet class'ı 3 bilgi istiyor Yolcu,Ucus,Koltuk numarası
# 1) Yolcu için yolcu class'ını çağırıp yolcumuzu oluşturuyoruz -> Yolcu("Alperen","Ağa",12456)
# 2) Ucuş için ucus class'ını çağırıp yolcumuzu oluşturuyoruz -> Ucus(Sehir("Ankara"),Sehir("İzmir"),datetime(2019,6,10,7,00))
# 3) Koltuk numarası için string olarak koltuk numarasını giriyoruz -> "A5"

def Main():
    
    # ========= City Lists =========
    se = ["Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin",
    "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale",
    "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir",
    "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "Mersin", "İstanbul", "İzmir", 
    "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", 
    "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya",
    "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak",
    "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak",
    "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"]
    # ========= End of List =========

    # ========= Creating City List w/'Sehir' class =========
    sehirler = list()
    for i in se:
        sehirler.append(Sehir(i))
    # For döngüsünün amacı; Bütün şehirleri Sehir class'ına obje olarak atamak

    # ========= Creating 'Bilet' - 2 =========
    yolcu = Yolcu("Alperen","Ağa",123456)
    pegasus = Pegasus()
    ucus1 = pegasus.UcusOlustur(sehirler[5],sehirler[34],datetime(2019,6,20,7,40))
    bilet2 = pegasus.BiletAl(yolcu,ucus1,"A5")
    print(bilet2)

    # ========= Using Methods =========
    pegasus.rotar(ucus1,40)
    print(bilet2)
    ucus2 = Ucus(sehirler[8],sehirler[78],datetime(2019,5,14,8,50))
    x = Bilet("Ahmet",ucus2,"C5")
    pegasus.BiletIptal(x)
    pegasus.BiletIptal(bilet2)

if __name__ == "__main__":
    Main()


# ========= Code Comment =========
#   
# 1) Bu kod, kabaca bir Hava Şirketinin bilet alma sisteminin basit prototipidir 
# 2) Kodun kullanımı için basitçe aşağıdaki adımları izleyin:
#   a) Main() fonksiyonunun içine girin
#   b) Sırayla; yolcu,pegasus,ucus ve bilet değişkenleri oluşturun
#   c) yolcu değişkenine, Yolcu class'ını kullanarak bir atama yapın
#   d) pegasus değişkenine, Pegasus class'ını kullanarak boş bir atama yapın
#   e) ucus değişkenine, Ucus class'ını kullanarak bir atama yapın
#       (Dikkat! : Ucus class'ının atamasını yaparken ilk 2 argümanı Sehir() class'ını kullanarak Yapınız)
#   f) bilet değişkenine, pegasus değişkeninizin .BiletAl() fonksiyonunu kullanarak sırayla değişkenlerinizi yerleştirin
#   SON ADIM: print(bilet) fonskiyonunu kullanarak bilet bilgilerinizi görebilirsiniz
# 3) Kodun içindeki bütün değişkenler encapsulation ile kapsüllenmiş ve ulaşılmaz haldedir
# 4) Kodu inceleyerek metodları öğrenebilir ve kullanabilirsiniz

# Writed by Alperen 