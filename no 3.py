class Shape:
    width = 0
    def __init__(self, width):
        self.width = width
        
class Square(Shape):
    name = "Shape"
    def get_area(self):
        return self.width ** 2
        
class Triangle(Shape):
    name = "Triangle"
    height = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return 0.5 * self.width * self.height
SquareX=Square(5)
print(f"Luas {SquareX.name} adalah {SquareX.get_area()}")

TriangleY = Triangle(5, 3)
print(f"Luas {TriangleY.name} adalah {TriangleY.get_area()}")

        

    
    