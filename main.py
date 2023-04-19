class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def combine(self, other, op):
        if op == "+":
            new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        elif op == "-":
            new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        else:
            raise ValueError("Unsupported operation")

        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def inverse(self):
        return Fraction(self.denominator, self.numerator)


f1 = Fraction(2, 4)
f2 = Fraction(3, 6)

if __name__ == '__main__':
    # str
    print(f1.numerator, f1.denominator)
    print(f2.numerator, f2.denominator)

    # add
    f3 = f1.combine(f2, "+")
    print(f3)

    # sub
    f4 = f1.combine(f2, "-")
    print(f4)

    # inverse
    f5 = f1.inverse()
    print(f5)
