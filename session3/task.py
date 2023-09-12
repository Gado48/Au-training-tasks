from math import sqrt

class ComplexNumbers:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return ComplexNumbers(real_part, imag_part)

    def __sub__(self, other):
        real_part = self.real - other.real
        imag_part = self.imag - other.imag
        return ComplexNumbers(real_part, imag_part)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumbers(real_part, imag_part)

    def __div__(self, other):
        dom = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / dom
        imag_part = (self.imag * other.real - self.real * other.imag) / dom
        return ComplexNumbers(real_part, imag_part)

    def mod(self):
        return sqrt(self.real**2 + self.imag**2)

    def __rep__(self):
        if self.imag == 0:
            return f"{self.real}+0.00i"
        elif self.real == 0:
            return f"0.00+{self.imag}i"
        else:
            return f"{self.real}+{self.imag}i"

c = ComplexNumbers(3, 2)
d = ComplexNumbers(-4, -5)

print(c + d)
print(c - d)
print(c * d)
print(c / d)
print(c.mod())
print(d.mod())
