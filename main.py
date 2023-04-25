class Fraction:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def __add__(self, other):
        new_numerator = (self.__numerator * other.__denominator) + (other.__numerator * self.__denominator)
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = (self.__numerator * other.__denominator) - (other.__numerator * self.__denominator)
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator, new_denominator)

    def inverse(self):
        return Fraction(self.__denominator, self.__numerator)

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        if value == 0:
            raise ValueError("Denominator cannot be zero")
        self.__denominator = value


f1 = Fraction(1, 2)
f2 = Fraction(2, 4)

if __name__ == '__main__':
    # str
    print(f1.numerator, f1.denominator)
    print(f2.numerator, f2.denominator)

    # add
    f3 = f1 + f2
    print(f3)

    # sub
    f4 = f1 - f2
    print(f4)

    # inverse
    f5 = f1.inverse()
    print(f5)
