class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)

print(f"c1 = {c1}")
print(f"c2 = {c2}")

sum_result = c1 + c2
print(sum_result)

sub_result = c1 - c2
print(sub_result)

mul_result = c1 * c2
print(mul_result)
