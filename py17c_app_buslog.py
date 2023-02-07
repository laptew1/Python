from py17a_app_dal import getAllProducts, getProductsByFirstLetters

products = getAllProducts()

def getProducts():
    return products

# Клиентская фильтрация
def getProductsByLetters(letters):
    # results = []
    # for p in products:
    #     if p["name"].upper().find(letters.upper()) == 0:
    #         results.append(p)
    # return results

    # напишите в одну строку (11:00)
    return list(filter(lambda p: p["name"].upper().find(letters.upper()) == 0, products))

if __name__ == "__main__":
    print(getProductsByLetters("b"))