from py17c_app_buslog import getProducts, getProductsByLetters
import sys

print(sys.argv)

# filter = input("Введите первые буквы названия товара: ")
filter = sys.argv[1]
# filter = 'b'

results = getProductsByLetters(filter)

print(f"\nНайдено товаров: {len(results)}\n")
for p in results:
    print(f"{p['name']:40}{p['price']}")