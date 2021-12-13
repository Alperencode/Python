# %%
print("*"*65)
print(" "*22,"Yüzyıl Hesaplama Programı")
print("*"*65)
print("")
print("Programı çalıştırmak için yil() yazınız!")
print("Not: Parantezin içine öğrenmek istediğiniz yılı giriniz")
print("")

# İndex code

def yil(yil):
    if(type(yil)==int):
        yil = str(yil)
        if(len(yil)<=2):
            print("1. Yüzyıl")
        else:
            if(len(yil)<=3):
                if(yil[1] and yil[2]) == "0":
                    print("yil[0]",". Yüzyıl",sep="")
                else:
                    yil1 = yil[0]
                    yil1 = int(yil1)
                    print(yil1+1,". Yüzyıl",sep="")
            else:
                if(int(yil)<100):
                    print("1. Yüzyıl")
                else:
                    if(yil[1:]) == "000":
                        print(yil[0:2],". Yüzyıl",sep="")
                    else:
                        yil2 = yil[0:2]
                        yil2 = int(yil2)
                        print(yil2+1,". Yüzyıl",sep="")
    else:
        print("Lütfen bir sayı giriniz")

# Writed by Alperen
