import subprocess as sp
import time
books = list()
cl = sp.call('cls',shell=True)
menu = """
[0] Show books
[1] Add book
[2] Delete book
[3] Quit

"""
def addBook():
    sp.call('cls',shell=True)
    print("===== Add New Book ======\n\n")
    i = 0
    numb = 1
    sp.call('color a',shell=True)
    for y in books:
        print(numb,")"," Name: ",books[i],sep="")
        i += 1  
        numb += 1
    print("")
    newbook = input("Please enter your book name: ")
    for book in books:
        if book == newbook:
            print("\a\nThis book already added")
            time.sleep(1.5)
            main()
            del newbook
        else:
            pass
    try:
        books.append(newbook)
        print("\nBook added successfully!")
        time.sleep(1.5)
        main()
    except:
        print("\a\nBook cant add.Please try again...")
        time.sleep(1.5)
        main()

def deleteBook():

    sp.call('cls',shell=True)
    print("===== Books in Library ======\n\n")
    sp.call('color a',shell=True)
    i = 0
    numb = 1
    for y in books:
        print(numb,")"," Name: ",books[i],sep="")
        i += 1  
        numb += 1
    if i == 0:
        inp2 = input("Your Library is empty\n\nPress enter for home page: ")
        if inp2 == True:
            print("\n You are going to home page...")
            time.sleep(1.5)
            main()
            del inp2
        else:
            print("\n You are going to home page...")
            time.sleep(1.5)
            main()
            del inp2
    print("")
    willdelete = input("Please enter book 'name' for delete book: ")
    try:
        books.remove(willdelete)
        print("\nBook removed successfully!")
        time.sleep(1.5)
        del willdelete
        deleteBook()
    except:
        print("\a\nBook didn't removed. Please try again...")
        time.sleep(1.5)
        del willdelete
        main() 
        
def showBooks(): 

    sp.call('cls',shell=True)
    print("===== Books ======\n\n")
    sp.call('color a',shell=True)
    q = 0
    for z in books:
        q += 1
    print("You have",q,"book in library\n")
    i = 0
    numb = 1
    for y in books:
        print(numb,")"," Name: ",books[i],sep="")
        i += 1  
        numb += 1
    print("")
    loop1 = True
    while loop1 == True:
        try:
            inp1 = input("Press enter for Home page: ")
            if(inp1 == True):
                loop1 = False
                print("\nYou are going to Home Page...")
                time.sleep(1.5)
                main()
            else:
                loop1 = False
                print("\nYou are going to Home Page...")
                time.sleep(1.5)
                main()
        except:
            loop1 = False
            print("\nYou are going to Home Page...")
            time.sleep(1.5)
            main()
    del inp1

def main():
    sp.call('cls',shell=True)
    sp.call('color B',shell=True)
    print("====== Library ======")
    print(menu)
    x = input("Answer:")
    x = str(x)
    try:
        if "0" in x:
            print("\nYou are going to Library...")
            time.sleep(1.5)
            showBooks()
        elif "1" in x:
            print("\nYou are going to Add New Book...")
            time.sleep(1.5)
            addBook()
        elif "2" in x:
            print("\nYou are going to Delete Book...")
            time.sleep(1.5)
            deleteBook()
        elif "3" in x:
            print("\a\nGoodBye!")
            time.sleep(1.5)
            sp.call('exit',shell=True)
        else:
            print("\a\nPlease select options")
            time.sleep(1.5)
            main()
        del x
    except:
        print("\a\nSomething is wrong.Please try again")
        time.sleep(1.5)
        main()
    
if __name__ == "__main__":
    main()