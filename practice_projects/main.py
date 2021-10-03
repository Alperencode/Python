# Kütüphane/Modüller
import random  # random sayı üretmek için
import os   # ekranı temizlemesi için
import time # Programın beklemesi için

# Not:
# Print'lerin içindeki \n satır atlaması için 'newline' demek 
# input alırken yazdığım int() kullanıcının sayı değeri girmesi için sayı girmezse program hata mesajı verip yeniden çalışıyor
# printlerin başındaki f"" string içerisine değişken yazmamı sağlıyor {} içine değişken ismini yazıyorum
# time.sleep()'ler programın beklemesi için


# Üretim Fonksiyonu
def Uretim():
    print("\nGramaj Hesabı için\n")
    
    # Kullanıcı girişlerini alıyorum ve değişkene atıyorum
    pi = 3.14
    r = int(input("r değerini giriniz:\n>"))
    ozgulAğırlık = int(input("\nÖzgül Ağırlık değerini giriniz:\n>"))
    uzunluk = int(input("\nUzunluk değerini giriniz:\n>"))
    r2 = r*r

    # Hesaplamalar
    gramaj = (pi*r2) * ozgulAğırlık * (uzunluk/1000000)
    print(f"\nÜrünün gramajı {gramaj} kilogramdır\n")
    
    hammaddeFiyatı = int(input("Hammadde fiyatını giriniz:\n>"))
    fiyat = gramaj * hammaddeFiyatı
    adet = int(input("\nKaç adet üretmek istediğinizi giriniz:\n>"))

    toplam_maliyet = (fiyat * adet) + ((fiyat*10) / 100)
    print(f"\nToplam maliyet {toplam_maliyet}Tl'dir\n")
    
    # Programın beklemesi için boş input
    input("Başka bir ürünü sorgulamak için Enter'a basınız...")


# Programın sonsuz döngüde çalışması için while True döngüsü içine yazdım
while True:
    # Try-except bloğu kullanıcının integer girip girmediğini kontrol ediyor
    try:
        os.system('cls')  # Ekranı temizlemesi için  
        stokKodu = int(input("Stok kodunu giriniz:\n>YM-5A-"))  # Stok kodunu alıyorum
        stokDeğeri = random.randint(1,50)   # Random bir stok değeri üretiyorum 1-50 arasında burayı değiştirebilirsin istediğin gibi
        print(f"\nYM-5A-{stokKodu} ürününden stokta {stokDeğeri} adet kalmıştır.")

        # Stok değeri 30'dan az ise:
        # Program üretim fonksiyonuna giriyor
        # Değil ise üretim yapmak istiyor musunuz diye soruyor
        if stokDeğeri < 30: 
            print("Stok sayınız 30'un altında, Üretim programına yönlendiriliyorsunuz...")
            Uretim()
        else:
            secim = input("Stok sayınız 30'un üstünde. Üretim yapmak istiyor musunuz?\n>")
            # Cevabın içinde evet var ise yeniden üretime giriyor
            # yok ise program başa dönüyor
            if "evet" in secim: 
                Uretim()
            else:   
                print("\nStok sorgulama ekranına dönülüyor...")
                time.sleep(1.5)
    except:
        print("\nLütfen bir sayı değeri giriniz...")
        time.sleep(1.5)