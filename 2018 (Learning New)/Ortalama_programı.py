# ortalama
print("*"*48)
print("\t1. YAZILILAR ORTALAMA HESAPLAMA")
print("*"*48)
# kullanıcıdan istenen: AD
ad=input("Başlamadan Önce Adınızı Giriniz:")

# kullanıcıdan istenen: NOT 
def nothesaplama():
    print("Notları Sayı Olarak Girdiğinden Emin Ol!")

    edebiyat = 1
    aedebiyat=int(input("Edebiyat Notunuzu Giriniz:"))
    while edebiyat == 1:
        if(aedebiyat>100):
            print("Lütfen 100'den küçük bir sayı giriniz")
            aedebiyat=int(input("Edebiyat Notunuzu Giriniz:"))
        else:
            bedebiyat=5*aedebiyat
            edebiyat = 0

    din = 1
    adin=int(input("Din Kültürü Notunuzu Giriniz:"))
    while din == 1:
        if(adin>100):
            print("Lütfen 100'den küçük bir sayı giriniz")
            adin=int(input("Din Kültürü Notunuzu Giriniz:"))
        else:
            bdin=2*adin
            din = 0

    tarih = 1
    atarih=int(input("Tarih Notunuzu Giriniz:"))
    while tarih == 1:
        if(atarih>100):
            print("Lütfen 100'den küçük bir sayı giriniz")
            atarih=int(input("Tarih Notunuzu Giriniz:"))
        else:
            tarih = 0
            btarih=2*atarih


    cografya = 1
    acografya=int(input("Coğrafya Notunuzu Giriniz:"))
    while cografya == 1:
        if(acografya>100):
            print("Lütfen 100'den küçük bir sayı giriniz")
            acografya=int(input("Coğrafya Notunuzu Giriniz:"))
        else:
            cografya = 0
            bcografya=2*acografya

    matematik = 1
    amatematik=int(input("Matematik Notunuzu Giriniz:"))
    while matematik == 1:
        if(amatematik>100):
            print("Lütfen 100'den küçük bir sayı giriniz")
            amatematik=int(input("Matematik Notunuzu Giriniz:"))
        else:
            bmatematik=6*amatematik
            matematik = 0

    fizik = 1
    afizik=int(input("Fizik Notunuzu Giriniz:"))
    while fizik == 1:
        if(afizik>100):
            print("Lütfen 100'den küçük bir sayı giriniz")
            afizik=int(input("Fizik Notunuzu Giriniz:"))
        else:
            fizik = 0
            bfizik=2*afizik

    kimya = 1
    akimya=int(input("Kimya Notunuzu Giriniz:"))
    while kimya == 1:
        if(akimya>100):
            print("Lütfen 100'den küçük bir sayı giriniz")
            akimya=int(input("Kimya Notunuzu Giriniz:"))
        else:
            kimya = 0
            bkimya=2*akimya

    biyoloji = 1
    abiyoloji=int(input("Biyoloji Notunuzu Giriniz:"))
    while biyoloji == 1:
        if(abiyoloji>100):
            print("Lütfen 100'den küçük bir sayı giriniz")
            abiyoloji=int(input("Biyoloji Notunuzu Giriniz:"))
        else:
            biyoloji = 0
            bbiyoloji=2*abiyoloji

    felsefe = 1
    afelsefe=int(input("Felsefe Notunuzu Giriniz:"))
    while felsefe == 1:
        if(afelsefe>100):
            print("Lütfen 100'den küçük bir sayı giriniz")
            afelsefe=int(input("Felsefe Notunuzu Giriniz:"))
        else:
            felsefe = 0
            bfelsefe=2*afelsefe

    ingilizce = 1
    aingilizce=int(input("İngilizce Notunuzu Giriniz:"))
    while ingilizce == 1:
        if(aingilizce>100):
            print("Lütfen 100'den küçük bir sayı giriniz")
            aingilizce=int(input("İngilizce Notunuzu Giriniz:"))
        else:
            ingilizce = 0
            bingilizce=4*aingilizce

    almanca = 1
    aalmanca=int(input("Almanca Notunuzu Giriniz:"))
    while almanca == 1:
        if(aalmanca>100):
            print("Lütfen 100'den küçük bir sayı giriniz")
            aalmanca=int(input("Almanca Notunuzu Giriniz:"))
        else:
            almanca = 0
            balmanca=2*aalmanca

    beden = 1
    abeden=int(input("Beden Eğitimi Notunuzu Giriniz:"))
    while beden == 1:
        if(abeden>100):
            print("Lütfen 100'den küçük bir sayı giriniz")
            abeden=int(input("Beden Eğitimi Notunuzu Giriniz:"))
        else:
            beden = 0
            bbeden=2*abeden

    gorsel = 1
    agorsel=int(input("Görsel/Müzik Notunuzu Giriniz:"))
    while gorsel == 1:
        if(agorsel>100):
            print("Lütfen 100'den küçük bir sayı giriniz")
            agorsel=int(input("Görsel/Müzik Notunuzu Giriniz:"))
        else:
            gorsel = 0
            bgorsel=2*agorsel

    sanat = 1
    asanat=int(input("Sanat Tarihi Notunuzu Giriniz:"))
    while sanat == 1:
        if(asanat>100):
            print("Lütfen 100'den küçük bir sayı giriniz")
            asanat=int(input("Sanat Tarihi Notunuzu Giriniz:"))
        else:
            sanat = 0
            bsanat=2*asanat

    bilgisayar = 1
    abilgisayar=int(input("Bilgisayar Notunuzu Giriniz:"))
    while bilgisayar == 1:
        if(abilgisayar>100):
            print("Lütfen 100'den küçük bir sayı giriniz")
            abilgisayar=int(input("Bilgisayar Notunuzu Giriniz:"))
        else:
            bilgisayar = 0
            bbilgisayar=2*abilgisayar

    # işlemler
    toplam=bedebiyat+bdin+btarih+bcografya+bmatematik+bfizik+bkimya+bbiyoloji+bfelsefe+bingilizce+balmanca+bbeden+bgorsel+bsanat+bbilgisayar
    sonuc=toplam/39
    print(ad,"1. Yazılılarınızın Ortalaması:",sonuc)
    if(sonuc>=85):
        print("Takdir Belgesi Kazandın",ad,"Tebrikler!")
    if(85>sonuc>=70):
        print("Teşekkür Belgesi Kazandın",ad+"!")
    if(70>sonuc):
        print("Belge Kazanamadın",ad,".Bidahaki sefere daha çok çalış!")

nothesaplama()


# Writed by Alperen
