import time
from threading import Thread, Lock


class Meter:

    def __init__(self):
        self.results = {}
        self.lock = Lock()

    def measure(self, n: int) -> int:
        time.sleep(3)
        result = n * 10
        return n

    def output_to_console(self, n: int):
        result = self.measure(n);
        self.lock.acquire()
        print(n, result)
        self.lock.release()

    def collect_result(self, n):
        result = self.measure(n);
        self.lock.acquire()
        self.results[n] = result
        self.lock.release()

if __name__ == "__main__":

    meter = Meter()

    # for n in range(1, 10):
    #     result = meter.measure(n)
    #     print(n, result)

    pool: list[Thread] = []

    for n in range(1, 10):
        # thread = Thread(target=meter.measure, args=(n, ))
        #thread = Thread(target=meter.output_to_console, args=(n,))
        thread = Thread(target=meter.collect_result, args=(n,))
        pool.append(thread)
        thread.start()

    # time.sleep(3.5)

    # while len(meter.results) < 9:
    #     time.sleep(0.1)

    for thread in pool:
        thread.join()

    # print(meter.results)
    for n in range(1, 10):
        print(n, meter.results[n])