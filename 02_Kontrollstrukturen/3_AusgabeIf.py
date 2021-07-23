a = True
b = False
numbero = 0

if a == b:
    print("Aha! True ist gleich False!")
elif not a or b:
    print("nicht a oder b")
elif (a and not b) and not numbero:
    print("Komplizierte Bedingung hat True ergeben")
else:
    print("Keine Bedingung hat True ergeben...")