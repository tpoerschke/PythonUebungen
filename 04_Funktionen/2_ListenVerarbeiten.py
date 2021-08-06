
def request_user_input(message):
    print(message)
    return input(">> ")

def parse_list(input_str):
    return list(map(int, input_str.split(",")))
    # Der obige Ausdruck als Schleifen-Konstrukt:
    # int_list = []
    # for num in input_str.split(","):
    #     int_list.append(int(num))
    # return int_list

def parse_user_choice(input_str):
    choice = int(input_str)
    if choice < 1 or choice > 4:
        raise ValueError()
    return choice

def action_sum(user_list):
    return sum(user_list)
    
def action_remove_duplicates(user_list):
    # In einer Menge (set) kommt jedes Element
    # genau einmal vor, so kann diese Eigenschaft
    # hier genutzt werden, um Duplikate zu entfernen.
    return list(set(user_list))

def action_find_duplicates(user_list):
    counting_dict = {}
    # Die Häufigkeit einer Zahl in der Liste ermitteln
    for number in user_list:
        counting_dict[number] = counting_dict.get(number, 0) + 1
    # Alle Dulikate zurückgeben
    return [number for number in counting_dict if counting_dict[number] > 1]

def action_sort(user_list):
    # Die eingebaute Funktion sorted
    # gibt eine sortierte Liste zurück
    return sorted(user_list)

def main():
    input_str = request_user_input("Geben Sie eine Liste ein (mit Komma getrennt):")
    # User-Input verarbeiten
    user_list = []
    try:
        user_list = parse_list(input_str)
    except:
        print("Fehler in der Eingabe! :/")
        return

    message = """Welche Aktion soll durchgeführt werden?
1: Summe bilden
2: Duplikate finden
3: Duplikate entfernen
4: Sortieren"""
    user_choice = request_user_input(message)
    try:
        user_choice = parse_user_choice(user_choice)
    except:
        print("Fehler bei der Eingabe! :/")
        return

    # Aktion auf die eingegebene Liste anwenden
    # (alternativ kann auch mit if-Statements
    # gearbeitet werden)
    actions = [
        action_sum, 
        action_find_duplicates, 
        action_remove_duplicates, 
        action_sort
    ]
    result = actions[user_choice-1](user_list)
    print(result)

if __name__ == "__main__":
    main()