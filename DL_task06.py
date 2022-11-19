
class bible:

    def __init__(text, adress: str) -> None:
        with open(adress, encoding="utf8") as f:
            text.adress = f.read()

    def number_words(text):
        result = len(text.adress.split())
        print('В тексте содержится', str(result), 'всего слов.')

    def sentence_length(text):
        result = len(text.adress.split()) // len(text.adress.split('.'))
        print('Средняя длина предложения составляет', str(result), 'слов(а).')

    def different_words(text):
        a = []
        for i in text.adress.split():
            a += i.split()
        print('В тексте содержится', len(set(a)), 'разных слов.')

    def punctuation_marks(text):
        znaki = [';', ':', '[', ']', '-', ',', '.', '!', '?']
        out_last = []
        for i in text.adress:
            if i in znaki:
                out_last.append(i)
        print('В тексте содержится', len(out_last), 'знаков препинания.')

if __name__ == "__main__":
    p1 = bible ("data/exodus.txt")
    p1.number_words()
    p1.sentence_length()
    p1.different_words()
    p1.punctuation_marks()

    #В тексте    содержится    25098    всего    слов.
    #Средняя    длина    предложения    составляет    33    слов(а).
    #В тексте    содержится    6063    разных    слов.
    #В тексте    содержится    5389    знаков    препинания.