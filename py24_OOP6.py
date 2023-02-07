# Проблема полиморфизма. В Питоне может быть реализована
# через наследование (как в статических языках) или через "утинe. типизацию"

class Animal:

    def eat(self):
        pass

    def voice(self) -> str:
        pass


class Cat(Animal):

    def eat(self):
        print("I eat mice")

    def voice(self) -> str:
        return "Meaou"


class Dog(Animal):

    def eat(self):
        print("I eat bones")

    def voice(self) -> str:
        return "Hab"


if __name__ == "__main__":

    zoo: list[Animal] = [
        Cat(),
        Dog()
    ]

    for animal in zoo:
        animal.eat()