with open("data/RusDictionary.txt", encoding="utf-8") as f:
    text = f.read()
words = text.split("\n")

# reversed = []
# for w in words:
#     if len(w) > 2:
#         reversed.append(w[::-1])

reversed = [w[::-1] for w in words]
print(reversed)

nums = [1, 2, 3, 4]
# Одной строкой кода преобразовать к списку квадратов (11:20)
print([x*x for x in nums])

