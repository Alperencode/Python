def main(): 
    x = input("Sayı 1: ")
    y = input ("Sayı 2: ")
    try:
        x = int(x)
        y = int(y)
        print(x/y)
    except:
        print("Please try again.")
        main()

main()