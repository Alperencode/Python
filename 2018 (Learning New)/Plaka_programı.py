iller = ['','ADANA', 'ADIYAMAN', 'AFYON', 'AĞRI', 'AMASYA', 'ANKARA', 'ANTALYA', 'ARTVİN',
'AYDIN', 'BALIKESİR', 'BİLECİK', 'BİNGÖL', 'BİTLİS', 'BOLU', 'BURDUR', 'BURSA', 'ÇANAKKALE',
'ÇANKIRI', 'ÇORUM', 'DENİZLİ', 'DİYARBAKIR', 'EDİRNE', 'ELAZIĞ', 'ERZİNCAN', 'ERZURUM', 'ESİKŞEHİR',
'GAZİANTEP', 'GİRESUN', 'GÜMÜŞHANE', 'HAKKARİ', 'HATAY', 'ISPARTA', 'MERSİN', 'İSTANBUL', 'İZMİR',
'KARS', 'KASTAMONU', 'KAYSERİ', 'KIRKLARELİ', 'KIRŞEHİR', 'KOCAELİ', 'KONYA', 'KÜTAHYA', 'MALATYA',
'MANİSA', 'KAHRAMANMARAŞ', 'MARDİN', 'MUĞLA', 'MUŞ', 'NEVŞEHİR', 'NİĞDE', 'ORDU', 'RİZE', 'SAKARYA',
'SAMSUN', 'SİİRT', 'SİNOP', 'SİVAS', 'TEKİRDAĞ', 'TOKAT', 'TRABZON', 'TUNCELİ', 'ŞANLIURFA', 'UŞAK',
'VAN', 'YOZGAT', 'ZONGULDAK', 'AKSARAY', 'BAYBURT', 'KARAMAN', 'KIRIKKALE', 'BATMAN', 'ŞIRNAK',
'BARTIN', 'ARDAHAN', 'IĞDIR', 'YALOVA', 'KARABÜK', 'KİLİS', 'OSMANİYE', 'DÜZCE']

print("Plaka numarasına göre şehir bulmak için plaka() yazıp parantez içine istediğiniz numarayı giriniz")
print("Şehir ismine göre plaka bulmak için sehir() yazıp parantez içine istediğiniz şehiri yazınız")
print("")

def plaka(x):
    if(type(x) == int):
        if(x > 81):
            print("Türkiye'de 81 il vardır")
        else:

            print(iller[x][0],iller[x][1:].lower(),sep="")
    else:
        print("Lütfen bir sayı giriniz")

def sehir(y):
    if(type(y) == str):
        sayac = 0
        y = y.upper()
        if y in iller:
            for q in iller:
                if y == q:
                    if(sayac < 10):
                        print("0",sayac,sep="")
                    else:
                        print(sayac)
                else:
                    sayac += 1
        else:
            print("Türkiye'de böyle bir il yok")
    else:
        print("Lütfen bir şehir ismi giriniz")    

