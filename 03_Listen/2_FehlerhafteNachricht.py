message = [50, 28, 68, 37, 90, 9, 92, 12, 99, 17, 20, 12, 100, 15, 89, 22, 31, 1, 111, 5, 101, 4, 88, 13, 96, 6, 23, 21, 24, 8, 69, 13, 202, 50, 55, 45, 71, 34, 60, 43, 97, 4, 81, 33, 31, 2]

decoded_message = ""

for i in range(0, len(message), 2):
    ascii_value = sum(message[i:i+2])
    decoded_message = decoded_message + chr(ascii_value)

print(decoded_message)