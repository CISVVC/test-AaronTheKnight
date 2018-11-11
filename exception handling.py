Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def __init__(self, num, den):
    num1, den1 = float(num).as_integer_ratio()
    den2, num2 = float(den).as_integer_ratio()
    self.numerator = num1 * num2
    self.denominator = den1 * den2
while absNum != absDen:
        if absNum > absDen:
            absNum = absNum - absDen
        elif absDen >= absNum:
            absDen = absDen - absNum
    return(absNum)
    class Rational:
    def __init__(self,numerator=0,denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        if denominator == 0:
            raise ZeroDivisionError("Error: cannot store number with 0 in denominator.")
        elif denominator < 0:
            if numerator < 0:
                self.denominator = -denominator
                self.numerator = -numerator
            else:
                self.numerator = numerator
                self.denominator = -denominator 
        if numerator != 0:
            com = gcd(numerator,denominator)
            numerator = numerator/com
            denominator = denominator/com
            self.numerator = numerator
            self.denominator = denominator
