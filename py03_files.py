with open("data/people.csv", encoding="utf-8") as f:
    text = f.read()

# print(text)

lines = text.split("\n")
# print(lines)
maxsalary = -100
richest = ""
for line in lines:
    # print(line)
    splitted = line.split(";")
    # print(splitted)
    firstname = splitted[0]
    lastname = splitted[1]
    salary = int(splitted[2])
    # print(lastname, salary)
    if salary > maxsalary:
        maxsalary = salary
        richest = f"{lastname}, {firstname}"

print(richest, maxsalary)

with open("data/richest.txt", "w", encoding="utf-8") as f:
    f.write(f"Самый высокоплачиваемый сотрудник: {richest}\n")
    f.write(f"Зарплата этого сотрудника: {maxsalary}")
