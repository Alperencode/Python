print("")
print("Temel Kavramlar:".upper())
print("Return: Geri Döndürmek")
print("Args(*args): Argümanlar")

print("")
print("2 Sayı Toplama Fonksiyonu - Print")

def toplama(x,y):
    toplam = x+y
    print(toplam)

toplama(5,10)

print("")
print("2 Sayı Toplama Fonksiyonu - Return".upper())

def topla(x,y):
    return x+y

print(topla(20,10))

print("")
print("Return ve Print Arasındaki Fark".upper())

print("Print:")
print("Dönen sonuç her zaman 'str' olacağı için sonuç döndürmek dışında kullanılamaz")
print("Aksi taktirde program int ve str değeri ile işlem yapmaya çalışıp hata verir")
print("Eğer fonksiyon str işlemi yapıyorsa her döndürdüğü değeri yeni satıra yazar")
print("Fonksiyon içinde olabildiğince az print kullanılması daha sağlıklıdır")
print("Döndürülen sonuç ekrana yazdırılır.")
print("")

print("Return:")
print("Dönen sonuç type'ı etkilemez.Yani çoklu işlemlerde rahatlıkla kullanılabilir")
print("Döndürülen değer ekrana yazdırılmaz. Fakat programın hafızasında tutulur.")
print("Döndürülen değerin türü bozulmayacağı için kullanılması daha sağlıklıdır")

print("")
print("Args Kullanımı".upper())
print("Args'ın fonksiyonlarda kullanılması içine değişken sayıda eleman almasını sağlar")
print("Örneğin bir toplama işlemini 2 argümanlı bir fonksiyon şeklinde yazarsak")
print("Fonksiyon zorunlu 2 argüman arayacak ve 2'den fazla argüman kabul etmeyecektir.")
print("Fakat *args kullanıldığında fonksiyon girilenlerin hepsini 'args' adında bir listeye atar")
print("Dolayısıyla for döngüsü ile liste okutulduğunda program girilen bütün değerleri toplayabilir")
print("Veya kullanıcıdan sırayla bir değer istenilir (Örn: Adınız,numaranız,şifreniz) gibi")
print("Program içinde 'args' listesinin elemanlarını kontrol ederek işlem yapılabilir")

print("")
print("Args Örneği:".upper())

def toplam(*args):
    result = 0
    for i in args:
        result += i
    return result

print(toplam(10,20,30,40)) # İsterseniz 4 argüman alır
print(toplam(10))          # İsterseniz 1 argüman alır
print(toplam())            # İsterseniz argüman almaz (:
