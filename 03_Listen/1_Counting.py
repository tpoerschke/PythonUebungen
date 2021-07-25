import random

# formuliert als List Comprehension
numbers = [random.randint(0, 9) for _ in range(20)]

print(numbers)

# Die Häufigkeit der Ziffern bestimmen
counting_list = [0] * 10
for number in numbers:
    counting_list[number] += 1

for i in range(10):
    print(str(i) + ": " + str(counting_list[i]), end=", ")

print()