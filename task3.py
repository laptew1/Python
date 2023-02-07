with open("data/RusDictionary.txt", encoding="utf-8") as f:
    text = f.read()
words = text.strip().split("\n")


def word_game(base_word: str) -> list[str]:
    results = []
    for w in words:
        is_good = True
        for letter in w:
            if base_word.count(letter) < w.count(letter):
                is_good = False
        if is_good:
            results.append(w)
    return results


base_words = ['программа', 'удивительный', 'телескопический','частнопредпринимательский']
for w in base_words:
    result = word_game(w)
    print(w, len(result), result)

# for w in words:
#     print(w, len(word_game(w)))

# print(max(words, key=lambda w: len(word_game(w))))
