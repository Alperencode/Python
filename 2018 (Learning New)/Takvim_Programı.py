import calendar

print("*"*80)
print("\tTAKVİM PROGRAMI")
print("*"*80)
print("")
print("Programı Çalıştırmak için 'takvim(yıl,ay)' yazınız")
print("Örneğin; takvim(2019,3)")
print("")

def takvim(x,y):
    print(calendar.month(x,y))
