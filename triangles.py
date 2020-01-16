# coding: utf8
from shape import Shape

class Triangle(Shape):
    """
    Triangular shapes.
    """
    a = None
    b = None
    c = None

    def __init__(self, a, b, c):#, ha = 0, hb = 0, hc = 0):
        super().__init__()
        self.a = a
        self.b = b
	self.c = c

    def area(self):
        p = self.perimeter/2
        return (p*(p-self.a)(p-self.b)(p-self.c))*(1/2)# Heron's formula

    def perimeter(self):
        return self.a + self.b + self.c

    def checkIfTriangle(self):
        if
                raise ValueError
