import os
import datetime
from threading import Thread, Lock

lock = Lock()

class Meter:

    def __init__(self):
        self.results = {}
        self.lock = Lock()


    def recode(input: str, encoding_from: str = "windows-1251", encoding_to: str = "866" ) -> str:
        return input.encode(encoding_from).decode(encoding_to)


    def host_is_good(host: str) -> bool:
        cmd = f"ping {host}"
        result = Meter.recode(os.popen(cmd).read())
        return result.find("TTL") > 0


    def check_hosts(hosts: list[str], display_immediately: bool = False) -> dict[str, bool]:
        result = Meter.host_is_good(hosts)
        if display_immediately:
            if result:
                pass
            else:
                lock.acquire()
                print(f"host {hosts} is bad {datetime.datetime.now()}")
                f1.write(hosts + '   ' + str(datetime.datetime.now()) + '\n')
                lock.release()
        return result


if __name__ == "__main__":
    print("Checking...")

    with open("data/hosts.txt", encoding="utf8") as f:
        hosts = f.read().split()
    f.close()
    f1 = open("data/log.txt", 'w')

    meter = Meter()
    pool: list[Thread] = []
    for n in hosts:
        thread = Thread(target=Meter.check_hosts, args=(n, True))
        thread.start()