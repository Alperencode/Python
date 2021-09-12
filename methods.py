#%%
class Book:
    def __init__(self,author,name,pageNum):
        self.__author = author
        self.__name = name
        self.__pageNum = pageNum

    def getAuthor(self):
        return self.__author
    
    def getName(self):
        return self.__name
    
    def getPageNum(self):
        return self.__pageNum
    
    def __str__(self):
        return "Author is: " + self.__author + " book name: " + self.__name + " number of pages: " + str(self.__pageNum)

    def __len__(self):
        return self.__pageNum

    def __del__(self):
        print("The book {} has deleted!".format(self.__name))

x = Book("Jon Duckett","HTML & CSS",460)

print(x)
del x




#%%
