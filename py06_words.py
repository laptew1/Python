with open("data/RusDictionary.txt", encoding="utf-8") as f:
    text = f.read()
words = text.split("\n")

# print(words[0:100])

# Вывести все слова-перевертыши (потоп, боб и т.д.) 10:12
for w in words:
    if  len(w)> 2 and w == w[::-1] and len(w) % 2 == 1:
        print(w)

# Вывести все пары слов-палиндромов (кот-ток, лаз-зал и т.д.)
# O(n2) - не годится
# for w1 in words:
#     for w2 in words:
#         if len(w1) > 2 and  w1 == w2[::-1]:
#             print(w1, w2)

# Решите с лучшей асимптотикой (10:36)
reversed = []
for w in words:
    if len(w) > 2:
        reversed.append(w[::-1])

# Вариант 1 - с применением множеств
# print(set(words).intersection(set(reversed)))

# Вариант 2 - с применением словаря
dict = {}
for w in words:
    if len(w) > 2:
        dict[w[::-1]] = w

for w in words:
    if w in dict:
        print(w, w[::-1])
