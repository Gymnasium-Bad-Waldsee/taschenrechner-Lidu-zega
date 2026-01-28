def add(a, b):
    """Gibt die Summe von a und b zurück."""
    return a + b

def subtraktion(a,b):
    return a - b

def multiplikation(a,b):
    return a * b

def division(a,b):
    return a / b

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
           print(f"Das Ergebnis ist: {subtraktion(num1,num2)}")
        
        elif choice == '3':
           print(f"Das Ergebnis ist: {multiplikation(num1,num2)}")
            
        elif choice == '4':
            print(f"Das Ergebnis ist: {division(num1,num2)}")
else:
    print("Ungültige Auswahl. Bitte wähle eine Operation zwischen 1 und 4.")
