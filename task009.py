import math
from datetime import datetime as dt
from threading import Thread, Lock

class Meter:

    def __init__(self, col_Th):
        self.summa = 0.0                #общая сумма
        self.summa_th = [0] * col_Th    #для подсчета сумм в каждом потоке
        self.lock = Lock()
        self.data = []
        for x in range(0, 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10):
            self.data.append(x)

    def counter(self, n, col_Th):
        for x in self.data:
            if x % col_Th == n:
                self.summa_th[n] += math.sin(x)

    def measure(self, n: int) -> int:
        for x in range(0, n):
            self.summa += self.summa_th[x]
        return self.summa


if __name__ == "__main__":

    start = dt.now()
    col_Thread = 16
    meter = Meter(col_Thread)
    pool: list[Thread] = []

    for n in range(0, col_Thread):
        thread = Thread(target=meter.counter, args=(n, col_Thread))
        pool.append(thread)
        thread.start()
    for thread in pool:
        thread.join()

    finish = dt.now()
    print(finish - start, meter.measure(col_Thread))

#без потокв 0:00:00.818630 1.6660756169488062
#1 поток    0:00:00.880350 1.6660756169488062
#2 потока   0:00:01.047154 1.666075616948771
#4 потока   0:00:01.235960 1.6660756169488669
#8 потоков  0:00:01.670719 1.6660756169487823
#16 потоков 0:00:02.547022 1.666075616948786
#Потоки выполняют вычисление и сохранение не пересекаясь,
# но при этом если на создание потока уходит приблизительно 0.1 секунды,
# то с нарастанием потоков время увеличивалось на эту пропорциональную величину,
# следовательно  работа происходит только в одном потоке с быстрым переключением между ними