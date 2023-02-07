def plus(x: int = 0, y: int = 0) -> int:
    result = x + y
    return result


print(plus(1, 2))
# print(plus("hello", "world"))

z = plus(1, 3)
print(plus(123))

def plus_minus(x: int = 0, y: int = 0) -> int:
    result0= x + y
    result1 = x - y
    return result0, result1

print(plus_minus(1, 2))

a, b = plus_minus(1,2)
print(a, b)

a, b = plus_minus(y=2, x=1)
print(a, b)

def summa(x: int, y: int, *args: int ) -> int:
    result = x + y
    for a in args:
        result += a
    return result

print(summa(1, 2, 3, 4, 5))

def dummy(x: str, **kwargs):
    print(f"x = {x}")
    for a in kwargs:
        print(a, kwargs[a])

dummy(123, lala=777, bubu=888)