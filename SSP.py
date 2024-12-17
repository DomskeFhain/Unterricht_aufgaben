import random

def spiel():
    gewinner = {"Benutzer": 0, "Computer": 0}

    while True:
        benutzer_wahl = input("Wähle Schere, Stein oder Papier: ")

        if benutzer_wahl not in ["schere", "stein", "papier"]:
            print("Ungültige Eingabe! Bitte wähle Schere, Stein oder Papier.")
            continue

        computer_wahl = random.choice(["schere", "stein", "papier"])
        print(f"Der Computer wählt: {computer_wahl.capitalize()}")

        if benutzer_wahl == computer_wahl:
            print("Unentschieden!")
        elif (benutzer_wahl == "schere" and computer_wahl == "papier") or \
             (benutzer_wahl == "stein" and computer_wahl == "schere") or \
             (benutzer_wahl == "papier" and computer_wahl == "stein"):
            print("Du hast gewonnen!")
            gewinner["Benutzer"] += 1
        else:
            print("Der Computer hat gewonnen!")
            gewinner["Computer"] += 1

        print(f"Aktueller Spielstand - Benutzer: {gewinner['Benutzer']}, Computer: {gewinner['Computer']}")

        weiterspielen = input("Möchtest du noch einmal spielen? (ja/nein): ")
        if weiterspielen != 'ja':
            break

    print("Danke fürs Spielen!")
    print(f"Endspielstand - Benutzer: {gewinner['Benutzer']}, Computer: {gewinner['Computer']}")

if __name__ == "__main__":
    spiel()