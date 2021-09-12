class Human:
    def __init__(self,name:str,surname:str,age:int):
        self.__name = name
        self.__surname = surname 
        self.__age = age 
    
    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname
    
    def getAge(self):
        return str(self.__age)
    
    def changeName(self,newname):
        self.__name = newname

    def __str__(self):
        return "Name: " + self.__name + " Surname: " + self.__surname + " Age: " + str(self.__age)
    
    def __len__(self):
        return self.__age
    
    def __del__(self):
        print("{} {} has deleted!".format(self.__name,self.__surname))

class Worker(Human):
    
    def __init__(self,name:str,surname:str,age:int,idno:int,p_lang:tuple):
        Human.__init__(self,name,surname,age)
        self.__idno = idno
        self.__p_lang = p_lang

    def getIdno(self):
        return self.__idno

    def getP_lang(self):
        return self.__p_lang

x = Worker("Zeynep","Ağa",17,1,("Python","Php","Arduino"))
print(x)
x.getName()
x.getP_lang()
x.changeName("Alperen")
x.getName()

