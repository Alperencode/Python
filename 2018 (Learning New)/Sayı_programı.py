import random

print("Bir Seviye Seçin!")
print("Seviye 1 için seviye1()")
print("Seviye 2 için seviye2()")
print("Seviye 3 için seviye3()")

# random.randint(1,101)


def seviye1():
    can = 4
    sev1 = 1
    sayi1  = random.randint(1,11)
    while sev1 == 1:
        x = int(input("1 ile 10 arasında bir sayı seçiniz:"))
        print("")
        if x > 10:
            print("Lütfen 1 ile 10 arasında bir sayı seçiniz!")
            break

        if x < 0:
            print("Lütfen 1 ile 10 arasında bir sayı seçiniz!")
            break

        kontrol1 = 1
        while kontrol1 == 1:
            if x == sayi1:
                print("TEBRİKLER BİLDİNİZ!")
                print("Cevap:",sayi1)
                kontrol1 = 0
                sev1 = 0
            if x < sayi1:
                can = can - 1
                print("Daha büyük bir sayı seçiniz")
                print("Kalan hakkınız:",can)
                x = int(input("Tekrar deneyiniz: "))
            if x > sayi1:
                can = can - 1
                print("Daha küçük bir sayı seçiniz")
                print("Kalan hakkınız:",can)
                x = int(input("Tekrar deneyiniz: "))
            if can == 0:
                print("Hakkınız bitti")
                print("Cevap:",sayi1)
                kontrol1 = 0
                sev1 = 0
            if x == sayi1 + 2 or sayi1 - 2 or sayi1 + 1 or sayi1 - 1 and x != sayi1:
                print("Çok Yaklaştın!")

def seviye2():
    can = 5
    sev2 = 1
    sayi2  = random.randint(1,51)
    while sev2 == 1:
        a = int(input("1 ile 50 arasında bir sayı seçiniz:"))
        print("")
        if a > 50:
            print("Lütfen 1 ile 50 arasında bir sayı seçiniz!")
            break

        if a < 0:
            print("Lütfen 1 ile 50 arasında bir sayı seçiniz!")
            break

        kontrol2 = 1
        while kontrol2 == 1:
            if a == sayi2:
                print("TEBRİKLER BİLDİNİZ!")
                print("Cevap:",sayi2)
                kontrol2 = 0
                sev2 = 0
            if a < sayi2:
                can = can - 1
                print("Daha büyük bir sayı seçiniz")
                print("Kalan hakkınız:",can)
                x = int(input("Tekrar deneyiniz: "))
            if a > sayi2:
                can = can - 1
                print("Daha küçük bir sayı seçiniz")
                print("Kalan hakkınız:",can)
                a = int(input("Tekrar deneyiniz: "))
            if can == 0:
                print("Hakkınız bitti")
                print("Cevap:",sayi2)
                kontrol2 = 0
                sev2 = 0
            if a == sayi2 + 2 or sayi2 - 2 or sayi2 + 1 or sayi2 - 1 and a != sayi2:
                print("Çok Yaklaştın!")


def seviye3():
    can = 10
    sayi3 = random.randint(1,101)
    sev3 = 1
    while sev3 == 1:
        z = int(input("1 ile 100 arasında bir sayı seçniz:"))
        print("")
        if z > 100:
            print("Lütfen 1 ile 100 arasında bir sayı seçiniz")
            break
        if z < 1:
            print("Lütfen 1 ile 100 arasında bir sayı seçiniz")
            break

        kontrol3 = 1
        while kontrol3 == 1:
            if z == sayi3:
                print("TEBRİKLER BİLDİNİZ!")
                print("Cevap:",sayi3)
                sev3 = 0
                kontrol3 = 0
            if z > sayi3:
                can = can - 1
                print("Daha küçük bir sayı seçiniz!")
                print("Kalan hakkınız:",can)
                z = int(input("Tekrar deneyiniz:"))
            if can == 0:
                print("Hakkınız bitti")
                print("Cevap", sayi3)
                sev3 = 0
                kontrol3 = 0
            if z < sayi3:
                can = can - 1
                print("Daha büyük bir sayı seçiniz!")
                print("Kalan hakkınız:",can)
                z = int(input("Tekrar deneyiniz:"))
            if z == sayi3 + 2 or sayi3 - 2 or sayi3 + 1 or sayi3 - 1 and z != sayi3:
                print("Çok Yaklaştın!")

# Writed by Alperen
