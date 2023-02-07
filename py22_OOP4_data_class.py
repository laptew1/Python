# Пример такк называемого "data class"

class Person:

    def __init__(self, firstname: str, lastname: str, salary: float) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


if __name__ == "__main__":
    p1 = Person(firstname="Yuri", lastname="Andrienko", salary=123456)
    # print(f"{p['firstName']} {p['lastName']} has salary {p['salary']}")
    print(f"{p1.firstname} {p1.lastname} has salary {p1.salary}")

    people = [
        p1,
        Person(firstname="Vasya", lastname="Pupkin", salary=77777),
        Person(firstname="Masha", lastname="Mashkina", salary=300000)
    ]

    print(max(people, key=lambda p: p.salary).lastname)

    for p in people:
        print(p)