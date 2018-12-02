class Point:        """représente un point dans l'espace"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

p1 = Point("2",5,6)
p2 = Point("5",2,3)
p3 = p1 + p2

print(p3.x, p3.y, p3.z)
