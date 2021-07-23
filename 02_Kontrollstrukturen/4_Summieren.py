
#n = 13
#i = 3
n = int(input("Obergrenze eingeben (inklusiv): "))
i = int(input("Untergrenze eingeben (inklusiv): "))
result = 0

while i < n + 1: # Obergrenze ist bei Summenzeichen inklusiv (daher +1)
    result += (i - 2) ** 2
    i += 1

print(f"Das Ergebnis ist {result}.")