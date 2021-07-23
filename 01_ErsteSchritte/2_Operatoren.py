# 1. Teil der Aufgabe
street = "Ottostraße"
number = 29
zipcode = 44867
city = "Bochum"

address = street + " " + str(number) + ", " + str(zipcode) + " " + city
print(address)

# 2. Teil der Aufgabe
x = 128
y = 16
y += 1

r1 = x // y
r2 = x % y

print("\n128 / 17:", r1) # Anmerkung: \n sorgt für einen Zeilenumbruch
print("Rest:", r2)