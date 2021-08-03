try:
    x = int(input("Geben Sie eine Zahl ein: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("Division durch 0!")
except:
    print("Ein Fehler ist aufgetreten!")
else:
    print("else-Zweig ausgeführt")
finally:
    print("finally-Zweig ausgeführt")