# people = [
#     ["Yuri", "Andrienko", 123456],
#     ["Vasya", "Pupkin", 77777],
#     ["Masha", "Mashkina", 300000]
# ]
#
# for p in people:
#     print(f"{p[0]} {p[1]} has salary {p[2]}")

# p = {"firstName": "Yuri", "lastName": "Andrienko", "salary": 123456}
# print(f"{p['firstName']} {p['lastName']} has salary {p['salary']}")

# people = [
#     {"firstName": "Yuri", "lastName": "Andrienko", "salary": 123456},
#     {"firstName": "Vasya", "lastName": "Pupkin", "salary": 77777},
#     {"firstName": "Masha", "lastName": "Mashkina", "salary": 300000},
# ]

# Представляем данные из хранилища в виде, удобном для дальнейшей обработки
with open("data/people.csv", encoding="utf-8") as f:
    text = f.read()
lines = text.split("\n")
people =[]
for line in lines:
    splitted = line.split(";")
    firstname = splitted[0]
    lastname = splitted[1]
    salary = int(splitted[2])
    people.append({"firstName": firstname, "lastName": lastname, "salary": salary})


# Обрабатываем эти данные на разные лады
richest = people[0]
for p in people:
    print(f"{p['firstName']} {p['lastName']} has salary {p['salary']}")
    if p['salary'] > richest['salary']:
        richest = p

print(f"Самый крутой сотрудник: {richest['lastName']}")

# Еще о множественных данных
person = {"firstName": "Yuri", "lastName": "Andrienko", "salary": 123456}
# for key in person:
#     print(key, person[key])
for key, value in person.items():
    print(key, value)

nums = (1, 2, 3) # кортеж (tuple)
# nums[0] = 777 # error
# nums.append(4) # error
print(nums[1], nums)

set1 = {1, 2, 3, 4, 2, 3}
set2 = {3, 4, 5}
print(set1)
print(set1.intersection(set2))

nums1 = [77, 7, 1, 2, 66, 5]
nums2 = [777, 66, 5, 4]

set1 = set(nums1)
set2 = set(nums2)
print(list(set1.intersection(set2)))

