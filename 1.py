sec = int(input("Введите секунды: "))
a = int(sec // 3600)
b = int((sec % 3600) // 60)
c = int((sec % 3600) % 60)
result = ["{} дней {} минут {} секунд".format(a, b, c)]

print(result)
