from py20_OOP2 import Arith


class ArithExtended(Arith):

    # Расширение предка
    def mult(self, x, y):
        return x * y * (1 - self.tax)

    # Перекрытие метода предка
    def minus(self, x, y):
        # return (x - y) * (1 - self.tax) - (x + y) * self.tax / 2
        return super().minus(x, y) - (x + y) * self.tax / 2

    # Перекрытие метода предка (дедушки)
    def __str__(self):
        return f"Класс фискальной арифметики при ставке {self.tax}"

if __name__ == "__main__":
    ae02 = ArithExtended()
    print(ae02.plus(1, 2), ae02.minus(1, 1))
    print(ae02)