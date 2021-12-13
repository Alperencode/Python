class Worker:
    """
        Writed for create easily worker information
    """
    
    species = "Programmer"
    extra = 1.8
    count = 0

    def __init__(self,name,surname,time,salary):
        self.name = name
        self.surname = surname
        self.time = time
        if self.time == "weekday" or "weekend":
            self.time = time
            if self.time == "weekday":
                self.choosen = 1
            elif self.time == "weekend":
                self.choosen = 2
        else:
            print("Please select weekday or weekend")
            self.time = "'none'"
        self.salary = salary
        Worker.count += 1

    def changetime(self):
        if(self.choosen == 1):
            self.time = "weekend"
        elif(self.choosen == 2):
            self.time = "weekday"

    def doraise(self):
        self.salary = self.salary * Worker.extra

    def changename(self,x):
        self.name = x

    def create_email(self):
        self.email = self.name.lower() + self.surname.lower() + "@hotmail.com"

print("")
print("Add new class:".upper())
print("Worker(name,surname,time,salary)")

Alperen = Worker("Alperen","Ağa","weekend",5000)
Mehmet = Worker("Mehmet","Ünlütürk","weekday",7500)
Danyal = Worker("Danyal","Babur","weekday",4000)

print("")

print("Self.name".upper())
print(Alperen.name)
print(Mehmet.name)
print(Danyal.name)

print("")

print("Self.time".upper())
print(Alperen.time)
print(Mehmet.time)
print(Danyal.time)

print("")

print("Self.changetime".upper())

Alperen.changetime()
print(Alperen.time)
Mehmet.changetime()
print(Mehmet.time)
Danyal.changetime()
print(Danyal.time)

print("")

print("Self.Money".upper())
print("Alperen:",Alperen.salary)
print("Mehmet:",Mehmet.salary)
print("Danyal:",Danyal.salary)

print("")

print("Self.doraise()".upper())

Alperen.doraise()
Mehmet.doraise()
Danyal.doraise()
print("Alperen",Alperen.salary)
print("Mehmet",Mehmet.salary)
print("Danyal",Danyal.salary)

print("")

print("Class.Count()".upper())
print(Worker.count)

print("")

print("Self.changename".upper())

Alperen.changename("Deneme1")
Mehmet.changename("Deneme2")
Danyal.changename("Deneme3")

print("Alperen:",Alperen.name)
print("Mehmet:",Mehmet.name)
print("Danyal:",Danyal.name)

Alperen.changename("Alperen")
Mehmet.changename("Mehmet")
Danyal.changename("Danyal")

print("")

print("Self.Species".upper())

print(Alperen.__class__.species)
print(Mehmet.__class__.species)
print(Danyal.__class__.species)

print("")

print("create_email".upper())
Alperen.create_email()
Mehmet.create_email()
Danyal.create_email()

print(Alperen.email)
print(Mehmet.email)
print(Danyal.email)

print("")

print("Writed by Alperen")

print("")
