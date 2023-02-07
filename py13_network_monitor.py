import os


def recode(input: str, encoding_from: str = "windows-1251", encoding_to: str = "866" ) -> str:
    return input.encode(encoding_from).decode(encoding_to)


def host_is_good(host: str) -> bool:
    cmd = f"ping {host}"
    result = recode(os.popen(cmd).read())
    return result.find("TTL") > 0


def check_hosts(hosts: list[str], display_immediately: bool = False) -> dict[str, bool]:
    results = {}
    for host in hosts:
        result =  host_is_good(host)
        results[host] = result
        if display_immediately:
            if result:
                print(f"host {host} is good")
            else:
                print(f"host {host} is bad")
    return results


if __name__ == "__main__":
    print("Checking...")
    hosts = ['127.0.0.1', 'ya.ru', 'trpr', '192.168.1.250', '192.168.1.1', '192.123.123.123']
    # print(check_hosts(hosts))
    # results = check_hosts(hosts)
    # for host in results:
    #     if results[host]:
    #         print(f"host {host} is good")
    #     else:
    #         print(f"host {host} is bad")

    check_hosts(hosts, display_immediately=True)

