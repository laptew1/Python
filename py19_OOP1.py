# Не совсем типичный, потому что для него нет понятия ОБЪЕКТ
class Arith:

    # поле класса
    tax = 0.2

    # метод класса
    def plus(x, y):
        return (x + y) * (1 - Arith.tax)

    def minus(x, y):
        return (x - y) *  (1 - Arith.tax)

if __name__ == "__main__":
    Arith.tax = 0.06
    print(Arith.plus(1, 2))