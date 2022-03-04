## Gerenators

def mygenerator(x):
    for i in range(x):
        yield i

values = mygenerator(100)
 
for i in values:
    print(i)

print(next(mygenerator))