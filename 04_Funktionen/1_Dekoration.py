
def calculate(a, b):
    return a + b, a - b

def decorate(stringi):
    stringi = "| " + stringi + " |"
    top_bottom = "+" + "-" * (len(stringi) - 2) + "+"
    stringi = top_bottom + "\n" + stringi + "\n" + top_bottom
    return stringi

a = 33
b = 66

s, d = calculate(a, b)

print("Addition:")
print(decorate(f"{a} + {b} = {s}"))
print("Subtraktion:")
print(decorate(f"{a} - {b} = {d}"))