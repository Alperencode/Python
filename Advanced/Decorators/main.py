# Decorators
def mydecorator(function):
    
    def wrapper(*args,**kwargs):
        print("Wrapper called") 
        function(*args,**kwargs)
    
    return wrapper

# So this func goes to mydecorator directly now 
@mydecorator
def helloWorld(name):
    print(f"Hello {name}")

helloWorld("Alperen")