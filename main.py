def add(a, b):
    """Gibt die Summe von a und b zurück."""
    return a + b

# Hier sollen die Schüler die Funktionen für Subtraktion, Multiplikation und Division selbst erstellen.
#kiiiiiii
print("Willkommen beim Taschenrechner!")
print("Wähle eine Operation:")
print("1. Addition")
print("2. Subtraktion")
print("3. Multiplikation")
print("4. Division")

choice = input("Gib die Nummer der gewünschten Operation ein (1/2/3/4): ")

if choice in ['1', '2', '3', '4']:
    try:
        num1 = float(input("Gib die erste Zahl ein: "))
        num2 = float(input("Gib die zweite Zahl ein: "))
    except ValueError:
        print("Ungültige Eingabe. Bitte gib Zahlen ein.")
    else:
        if choice == '1':
            print(f"Das Ergebnis ist: {add(num1, num2)}")
        elif choice == '2':
            # Hier soll die Subtraktionsfunktion aufgerufen werden
            pass
        elif choice == '3':
            # Hier soll die Multiplikationsfunktion aufgerufen werden
            pass
        elif choice == '4':
            # Hier soll die Divisionsfunktion aufgerufen werden
            pass
else:
    print("Ungültige Auswahl. Bitte wähle eine Operation zwischen 1 und 4.")
