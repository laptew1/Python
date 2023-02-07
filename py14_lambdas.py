from typing import Callable, Iterable

def f1(x=0):
    return 2 * x

print(f1(2))

# Функции - это объекты первого класса
f2 = f1
f3 = f2
print(f2, f3, f3(3), f1(3))

# Обобщенные функции - могут принимать другие функции в качестве аргументов


def f4(x: int, f: Callable[[int], int]) -> int:
    y = x + 1
    return f(y)

print(f4(4, f1))

# Лямбды
print(f4(5, lambda x: 2 * x))

# Практическое применение
data = [1, 2, 3, 4, 33, -44, 55, 6, 11]
# Нужно фильтровать список (числа больше 10)
# Классическое решение:
# results = []
# for x in data:
#     if x > 10:
#         results.append(x)
# print(results)

# Обобщенная функция для фильтрации
def myfilter(data, criteria):
    results = []
    for x in data:
        if criteria(x):
            results.append(x)
    return results

# 1. Пример использования с именованной функцией
def crit1(x):
    return x > 10
print(myfilter(data, crit1))

# 2. Пример использования с лямбдой:
print(myfilter(data, lambda x: x > 10))
print(myfilter(data, lambda x: x < 10))
print(myfilter(data, lambda x: x * x > 1000))

# Не надо изобретать велосипед: есть готовые функции
# для фильтрации, трансформации, сортировки и др.

print(list(filter(lambda x: x > 10, data)))
people = [
    {"firstName": "Yuri", "lastName": "Andrienko", "salary": 123456},
    {"firstName": "Vasya", "lastName": "Pupkin", "salary": 77777},
    {"firstName": "Masha", "lastName": "Mashkina", "salary": 300000},
]
# Отсортировать людей по возрастанию зарплат
results = sorted(people, key=lambda p: -p["salary"])
print(results)

# Вывести фамилию самого высокооплачиваемого сотрудника одной строкой кода (12:34)
print(sorted(people, key=lambda p: -p["salary"])[0]["lastName"])
print(max(people, key=lambda p: p["salary"])["lastName"])

# Как "молодежь" обходится без циклов

def foreach(data: Iterable, action: Callable) -> None:
    for x in data:
        action(x)

foreach([1, 2, 3], lambda x: print(x))

# Найти среднюю зарплату в people в одну строчку кода (9:44)
print(sum([p["salary"] for p in people]) / len(people))
salaries = list(map(lambda p: p["salary"], people))
print(sum(salaries) / len(people))


with open("data/RusDictionary.txt", encoding="utf-8") as f:
    text = f.read()
words = text.split("\n")

# Найти самое длинное слово в русском языке одной строкой кода (10:05):
print(max(words, key=lambda w: len(w)))
print(max(words, key=len))

