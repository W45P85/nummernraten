import random

top_of_range = input("Gib die höchste Zahl aller möglichen Zahlen ein: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Bitte gebe das nächste Mal eine Zahl größer als 0 ein.")
        quit()
else:
    print("Bitte gib das nächste Mal eine Zahl ein.")
    quit()

random_number = (random.randrange(top_of_range))
guesses = 0

while True:
    guesses += 1
    user_guess = input("Rate: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Bitte gib das nächste Mal eine Zahl ein.")
        continue
    
    if user_guess == random_number:
        print("Super! Du hast die richtige Zahl getippt. :)")
        break
    elif user_guess > random_number:
        print("Die Zahl ist zu groß.")
    else:
        print("Die Zahl ist zu klein.")

print(f"Du hast {guesses} Versuche benötigt.")
