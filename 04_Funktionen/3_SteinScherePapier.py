import random

FIGURES = {"stein": 1, "schere": 2, "papier": 3}
# Stein gewinnt gegen Schere, Schere gegen Papier und Papier gegen Stein
WIN_OUTCOMES = ((1, 2), (2, 3), (3, 1))

def get_user_choice():
    user_choice = input("STEIN, SCHERE oder PAPIER? ").lower()
    if user_choice in FIGURES:
        return user_choice, FIGURES[user_choice] 
    else:
        return None

def get_computer_choice():
    return random.choice(list(FIGURES.items()))

def evaluate(user_choice, computer_choice):
    if user_choice[1] == computer_choice[1]:
        return "Unentschieden!"
    else:
        eval_tuple = (user_choice[1], computer_choice[1])
        if eval_tuple in WIN_OUTCOMES:
            return "Gewonnen!"
        else:
            return "Verloren!"

def main():
    # User-Input
    user_choice = get_user_choice()
    if user_choice is None:
        exit("Falsche Eingabe :/")
    # Computer-"Input"
    computer_choice = get_computer_choice()

    print("AUSWERTUNG:")
    print(f"Spieler:   {user_choice[0].capitalize()}")
    print(f"Computer:  {computer_choice[0].capitalize()}")
    print("Ergebnis:", evaluate(user_choice, computer_choice))

if __name__ == "__main__":
    main()