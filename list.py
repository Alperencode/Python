print("Liste Fonksiyonları".upper())
print("")

liste = ["a","b","c"]

for i in dir(liste):
    if i[0] != "_":
        print(i)

print("")
print("APPEND")

print("append() öncesi:",liste)
liste.append("d")                   # liste += ["d"]
print("append() sonrası:",liste)

print("")
print("İNSERT")
print("İnsert() öncesi liste:",liste)
liste.insert(2, "i")                  # liste.insert(index, object)
print("İnsert() sonrası liste:",liste)

print("")
print("POP")
print("pop öncesi:",liste)
print("pop uygulanan:",liste.pop()) # argüman olarak index sayısı alır default olarak son elemanı alır
                                    # ve çıkarttığı elemanı return eder
print("pop sonrası",liste)

print("")
print("REMOVE")

print("remove öncesi:",liste)
liste.remove("b")               # argüman olarak liste elemanını alır fakat return etmez
print("remove sonrası:",liste)

print("")
print("İNDEX")

print(liste.index("a")) # liste index sayısını öğrenmek için

print("")
print("COUNT")

print(liste.count("a")) # liste içinde arama saydırmak istediğim elemanı fonksiyonun içine gönderiyorum

print("")
print("(-) İNDEX")

print(liste[-0]) # her elemanın 2 index'i var (-) ve (+) indexler

print("")
print("LEN FONSİYONU YAZMAK")

count=0            # Sayaç
for x in liste:    # For döngüsü ile listeyi saydırma
    count += 1     # Döngü her döndüğünde sayacı arttırma dolayısıyla liste elemanı kadar sayacın artması

print(count)

print("")
print("REVERSE")

liste.reverse()
print(liste)

print("")
print("SORT")

liste.sort()
print(liste)

print("")
print("NUMBER SORT")

liste2 = [6,5,2,4,1,3,7,6]

print(liste2)
liste2.sort()
print(liste2)

print("")
print("EXTEND")           # Listeye eleman ekleme

liste.extend("f")  # sadece 1 eleman
print(liste)

print("")

print("LEN FONKSİYONU YARATMAK")

print(liste.index(liste[-1]) + 1)  # listenin son index sayısına 1 ekleyerek toplam eleman sayısını buluyoruz

print("")

print("ÖNEMLİ!")
print("COPY ve Atamanın Farkı".upper())

print("")
print("X adında bir liste oluşturup içine iki eleman atadım")
x = list()
x.append("Alperen")
y = x
print("X ve Y'yi eşitledim")

print("")
print("X'e bir eleman daha ekleyip iki listeyi karşılaştırıyorum:")
x.append("Zeynep")
print("x:",x)
print("y:",y)

print("")
print("id:",id(x))
print("id:",id(y))

print("")
print("X'e Eklediğim eleman iki listeyede eklendi")
print("Ve aynı zamanda iki liste de hafızada aynı yeri tutuyor")
print("Yani X ve Y şu an bağlı iki eleman ve ikisininde id'si aynı")
print("Fakat '.copy()' fonksiyonunu kullanırsak X ve Y arasında bağlantı kurulmayacak")
print("Dolayısıyla Y sadece copy() fonksiyonunu yazdığımız satırdaki X'i kopyalayacak")
print("")

print("Q isimli bir liste oluşturuyorum:")
q = list()
print("Q listesine 1 eleman ekliyorum:")
q.append("Alperen")
print(q)

print("")
print("Q listesini  Z değişkenine copy() fonksiyonu ile kopyalıyorum")
z = q.copy()
print("q:",q)
print("z:",z)

print("")
print("Q listesine bir eleman daha ekliyorum ve iki listeyi karşılaştırıyorum:")
q.append("Zeynep")
print("q:",q)
print("z:",z)

print("")
print("q id:",id(q))
print("z id:",id(z))

print("")
print("Gördüğümüz gibi ikisinin arasında herhangi bir bağ kalmadı")
print("Sadece kopyaladığımız satırdaki elemanları aldı")
print("Aynı zamanda id'leri değişti yani artık hafızada farklı yerlere sahip")

print("")

print("Writed by Alperen")

print("")
