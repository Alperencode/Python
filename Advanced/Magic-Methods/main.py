# Dunders and Magic Methods
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"

    # manupilating length
    def __len__(self):
        return 10

    def __call__(self):
        print("Called Vector")

v1 = Vector(20, 30)
v2 = Vector(40, 50)
v3 = v1 + v2

print(len(v3))
print(v3)
v3()