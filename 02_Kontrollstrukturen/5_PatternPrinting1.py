UPPER_BOUND = 10

# Kompakte Lösung:
for i in range(1, UPPER_BOUND):
    print(str(i) * i, end=" ")

print() # Zeilenumbruch

# Alternative Lösung:
for i in range(1, UPPER_BOUND):
    for _ in range(i):
        print(i, end="")
    print(" ", end="")

print() # Zeilenumbruch