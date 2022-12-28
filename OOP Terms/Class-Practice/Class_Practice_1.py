class Worker:

    count = 0

    def __init__(self, name, time, salary):
        self.name = name
        self.time = time
        self.salary = salary
        Worker.count = Worker.count + 1 
    
    def NameTime(self):
        return self.name + " " + self.time
    
Calisan1 = Worker("Alperen","Freelance",5000)
Calisan2 = Worker("Efe","Haftasonu",4000)
Calisan3 = Worker("Umut","Haftaiçi",3500)
Calisan4 = Worker("Egemen","Freelance",4500)

liste = [Calisan1,Calisan2,Calisan3,Calisan4]

for each in liste:
    if each.salary > max_salary :
        max_salary = each.salary
        max_ = each

print(max_salary)

print(max_.NameTime())