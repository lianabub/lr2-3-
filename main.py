n = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))

apple = k // n
leftovers = k - apple*n

apple = k // n
print(apple)
print("По ", apple, "каждому школьнику.")
print(leftovers, "яблок останется в корзине.")