class Shape:
    def __init__(self,name):
        self.name = name
    
    def area(self):
        return 0



class Rectangle(Shape):
    def __init__(self,name,width,height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    



class Circle(Shape):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius


# shape = Rectangle("MyRectangle", 20, 10)
# print(f"{shape.name} area: {shape.area() }")
# shape1 = Circle("MyCircle", 12)
# print(f"{shape1.name} area: {shape1.area() }")

shapes = (Rectangle("MyRectangle", 20, 10),Circle("MyCircle", 12) )

for item in shapes:
    print(f"{item.name} area:{item.area()}")