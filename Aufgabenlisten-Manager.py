
aufgaben = []

def zeige_menü():
    """Zeige die Menüoptionen."""
    print("\nAufgabenlisten-Manager:")
    print("1. Aufgabe hinzufügen")
    print("2. Aufgaben anzeigen")
    print("3. Aufgabe als erledigt markieren")
    print("4. Beenden")

def aufgabe_hinzufügen():
    """Füge eine neue Aufgabe zur Liste hinzu."""
    aufgabe = input("Geben Sie die Aufgabe ein: ")
    aufgaben.append(aufgabe)
    print(f"Aufgabe hinzugefügt: {aufgabe}")

def aufgaben_anzeigen():
    
    if not aufgaben:
        print("Keine Aufgaben in der Liste.")
    else:
        print("\nIhre Aufgaben:")
        for i, aufgabe in enumerate(aufgaben, 1):
            print(f"{i}. {aufgabe}")

def aufgabe_als_erledigt_markieren():
    
    if not aufgaben:
        print("Keine Aufgaben zum Erledigen.")
        return
    
    aufgaben_anzeigen()
    try:
        aufgaben_nummer = int(input("Geben Sie die Nummer der zu erledigenden Aufgabe ein: "))
        if 1 <= aufgaben_nummer <= len(aufgaben):
            erledigte_aufgabe = aufgaben.pop(aufgaben_nummer - 1)
            print(f"Aufgabe erledigt: {erledigte_aufgabe}")
        else:
            print("Ungültige Aufgabennummer.")
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein.")


while True:
    zeige_menü()
    wahl = input("Wählen Sie eine Option (1-4): ")

    if wahl == "1":
        aufgabe_hinzufügen()
    elif wahl == "2":
        aufgaben_anzeigen()
    elif wahl == "3":
        aufgabe_als_erledigt_markieren()
    elif wahl == "4":
        print("Auf Wiedersehen!")
        break
    else:
        print("Ungültige Auswahl. Bitte geben Sie eine Zahl zwischen 1 und 4 ein.")
