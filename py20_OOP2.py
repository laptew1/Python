# Типичный класс, для которого важно понятие ОБЪЕКТ
class Arith:

    # конструктор класса (self - маркер "экземплярности")
    def __init__(self, tax = 0.2):
        # поле класса (относится к экземпляру класса)
        self.tax = tax

    # метод класса (self - маркер "экземплярности")
    def plus(self, x, y):
        return (x + y) * (1 - self.tax)

    def minus(self, x, y):
        return (x - y) * (1 - self.tax)

if __name__ == "__main__":
    # Создание экземпляров класса (=объектов)
    arith02 = Arith()
    arith006 = Arith(0.06)
    # arith006.tax = 0.06
    print(arith02.plus(1, 2), arith006.plus(1, 2))

    # В питоне всё - объекты или классы
    a = 123
    # print(a.to_bytes(...))
    s = "qwerty"
    print(s.upper())
