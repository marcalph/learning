from math import hypot, atan, sin, cos


class CustomComplex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def conjugate(self):
        return self.__class__(self.real, -self.imag)
    
    def argz(self):
        return atan(self.imag / self.real)
    
    def __abs__(self):
        return hypot(self.real, self.imag)
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.real}, {self.imag})"

    def __str__(self):
        return f"({self.real}{self.imag:+}j)"

    def __add__(self, other):
        real = imag = 0
        if isinstance(other, float) or isinstance(other, int):
            real = self.real + other
            imag = self.imag
        
        if isinstance(other, self.__class__):
            real += other.real
            imag += other.imag
        
        return self.__class__(real, imag)
    
    def __sub__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            real_part = self.real - other
            imag_part = self.imag

        if isinstance(other, CustomComplex):
            real_part = self.real - other.real
            imag_part = self.imag - other.imag

        return self.__class__(real_part, imag_part)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            real_part = self.real * other
            imag_part = self.imag * other

        if isinstance(other, CustomComplex):
            real_part = (self.real * other.real) - (self.imag * other.imag)
            imag_part = (self.real * other.imag) + (self.imag * other.real)

        return self.__class__(real_part, imag_part)
    
    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rsub__(self, other):
        # x - y != y - x
        if isinstance(other, float) or isinstance(other, int):
            real_part = other - self.real
            imag_part = -self.imag

        return self.__class__(real_part, imag_part)

    def __eq__(self, other):
        # Note: generally, floats should not be compared directly
        # due to floating-point precision
        return (self.real == other.real) and (self.imag == other.imag)

    def __ne__(self, other):
        return (self.real != other.real) or (self.imag != other.imag)

    def __pow__(self, other):
        r_raised = abs(self) ** other
        argz_multiplied = self.argz() * other

        real_part = round(r_raised * cos(argz_multiplied))
        imag_part = round(r_raised * sin(argz_multiplied))

        return self.__class__(real_part, imag_part)





if __name__ == "__main__":
    a = CustomComplex(1, 2)
    b = CustomComplex(3, -4)
    print(a)

print(b)