from fractions import Fraction


class Number():
    """ """

    def __init__(self, value_dec="", nemerator="", denominator=1):
        self.__value_dec = value_dec
        self.__nemerator = nemerator
        self.__denominator = denominator
        if value_dec != "":
            self.__nemerator = Fraction(value_dec).numerator
            self.__denominator = Fraction(value_dec).denominator
            self.__value_dec = self.__nemerator / self.__denominator
        else:
            if self.isfloat(nemerator) or self.isfloat(denominator):
                self.__value_dec = nemerator / denominator
                self.__nemerator = Fraction(self.__value_dec).numerator
                self.__denominator = Fraction(self.__value_dec).denominator
            self.__value_dec = nemerator / denominator

        """Перегрузки арифметический операторов"""

    def __add__(self, other):
        self.__value_dec = self.__value_dec + other.__value_dec
        self.__nemerator = Fraction(self.__value_dec).numerator
        self.__denominator = Fraction(self.__value_dec).denominator
        return self

    def __sub__(self, other):
        self.__value_dec = self.__value_dec - other.__value_dec
        self.__nemerator = Fraction(self.__value_dec).numerator
        self.__denominator = Fraction(self.__value_dec).denominator
        return self

    def __mul__(self, other):
        self.__value_dec = self.__value_dec * other.__value_dec
        self.__nemerator = Fraction(self.__value_dec).numerator
        self.__denominator = Fraction(self.__value_dec).denominator
        return self

    def __truediv__(self, other):
        self.__value_dec = self.__value_dec / other.__value_dec
        self.__nemerator = Fraction(self.__value_dec).numerator
        self.__denominator = Fraction(self.__value_dec).denominator
        return self

    def __pow__(self, other, modulo=None):
        self.__value_dec = self.__value_dec ** other.__value_dec
        self.__nemerator = Fraction(self.__value_dec).numerator
        self.__denominator = Fraction(self.__value_dec).denominator
        return self

        """Гетеры-сетеры"""

    def set_value_dec(self, v):
        self.__value_dec = v
        self.__nemerator = Fraction(v).numerator
        self.__denominator = Fraction(v).denominator

    def get_value_dec(self):
        return self.__value_dec

    def set_nemerator(self, n):
        if self.isfloat(n):
            self.__value_dec = n / self.__denominator
            self.__nemerator = Fraction(self.__value_dec).numerator
            self.__denominator = Fraction(self.__value_dec).denominator
        else:
            self.__nemerator = n

    def get_nemerator(self):
        return self.__nemerator

    def set_denominator(self, d):
        if self.isfloat(d):
            self.__value_dec = self.__nemerator / d
            self.__nemerator = Fraction(self.__value_dec).numerator
            self.__denominator = Fraction(self.__value_dec).denominator
        else:
            self.__denominator = d

    def get_denominator(self):
        return self.__denominator

    @staticmethod
    def isfloat(value):  # проверка на дробность
        try:
            float(value)
            return True
        except ValueError:
            return False

