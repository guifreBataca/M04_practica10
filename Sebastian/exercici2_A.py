def func(**valores):
    print(len(valores))
    for key, value in valores.items():
        print(value)
    print(valores.popitem())