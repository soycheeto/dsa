class Student():
    def __init__(self, name, USN):
        self.name = name
        self.USN = USN
    def print_properties(self):
        print(self.name)
        print(self.USN)


s1 = Student("Aarav Kumar", "1RVU23BSC001")
s2 = Student("Trisha D'Souza", "1RVU23BSC160")

s1.print_properties()
s2.print_properties()

#Create a class rectangle with attributes - length and breadth. Define two methods - find_area(self) and find perimeter(self). Create two instances and find the area and perimeter of the two instances.

class Rectangle():
    def __init__(self, length, breadth):
        self.length = int(length)
        self.breadth = int(breadth)
    def find_area(self):
        print(self.length  * self.breadth)
    def find_perimeter(self):
        print(2*(self.length + self.breadth))
    
r1 = Rectangle(2,3)
r2 = Rectangle(4,5)

r1.find_area()
r2.find_area()
r1.find_perimeter()
r2.find_perimeter()

#Create a class triangle with attributes - length  breadth, height. Define a method - find_area(self) Create two instances and find the area of the two instances.

class Triangle():
    def __init__(self, length, breadth, height):
        self.length = int(length)
        self.breadth = int(breadth)
        self.height = int(height)
    def find_area(self):
        print(0.5*self.breadth*self.height)

t1 = Triangle(1,2,3)
t2 = Triangle(4,5,6)

t1.find_area()
t2.find_area()

#Create a class complex number with attributes real and imaginary. Define a method to find the sum of a complex number

class Complex():
    def __init__(self, real, imaginary):
        self.real = int(real)
        self.imaginary = int(imaginary)
    def sum(self, num2):
        return Complex(self.real+num2.real, self.imaginary+num2.imaginary)
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = Complex(1,2)
c2 = Complex(3,4)
print(c1.sum(c2))



    
