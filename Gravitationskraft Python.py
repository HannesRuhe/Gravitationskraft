# Gravitationskraft:

# Variabeln: F = Gravitationskraft = graviKra
#            Fg = Gewichtskraft = gewiKra
#            G = Gravitationskonstante = graviKo
#            Ge = Gravitationskonstante Erde = graviKoE
#            m1 = Masse 1 in Kg = mass1
#            m2 = Masse 2 in Kg = mass2
#            r² = Abstand der Massen hoch 2 = abstand

# Texte:

einführung = """
    Hallo, hast du Lust die Anziehung
    zwischen zwei Objekten zu berechnen
    oder die Gewichtskraft von einem
    Körper zur Erde?
    
    Sicher nicht ...
    
    Deswegen hilft dir dieses Programm die
    Berechnungen automatisch durchzuführen.
    """

rechenarttext1 = """
    Möchtetst du die Anziehung
    zwischen zwei Objekten berechen?
    Drücke y (yes) oder n (no)
    """

rechenarttext2 = """
    Möchtetst du die Gewichtskraft
    zwischen einem Objekt und
    der Erde berechen?
    Drücke y (yes) oder n (no)
    """

print(einführung)

input("Bereit zum fortfahren? Drücke Enter.")

# while-Schleife

end = 1
while end == 1:

    import time # Zeitverzögerung aktivieren
    print("...")
    time.sleep(1) # Das Program muss "Laden"
    print("...")
    time.sleep(1) # Zeitverzögerung für 1 Sekunden anwenden
    print("...")
    time.sleep(1)

# Rechenart definieren:

    rechenart1 = input(rechenarttext1).lower()

    if rechenart1 == "y":
    
# Variabeln definieren:

        mass1 = float(input("Gib die Masse in Kg von deinem ersten Objekt an: "))
        mass2 = float(input("Gib die Masse in Kg von deinem zweiten Objekt an: "))
        abstand = float(input("Gib den Abstand deiner Objekte in Meter an: "))
    
# Berechnungen durchführen:
    
        rechenschritt1 = mass1 * mass2
        rechenschritt2 = rechenschritt1 / abstand
        graviKra = rechenschritt2 * 6.67e-11
            
        time.sleep(1) # Das Program muss "Laden"
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
    
        # Ausgabe:
        print("Die Anziehungskraft in Newton beträgt", graviKra)
        print("Das e in deiner Zahl steht für ~ hoch ~")
    
    
    elif rechenart1 == "n":
    
# Rechenart definieren:
    
        rechenart2 = input(rechenarttext2)
    
        if rechenart2 == "y":
        
# Variabeln definieren:
    
            mass1 = float(input("Gib die Masse in Kg von deinem Objekt an: "))
    
# Berechnungen durchführen:

            gewiKra = 9.81 * mass1
            
            time.sleep(1) # Das Program muss "Laden"
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            
            # Ausgabe
            print("Die Gewichtskraft in Newton beträgt", gewiKra)
        
# Wiederholungsschleife: (While-schleife)

    print("")
    print("Willst du das Programm beenden? Dann drücke y (yes).")      
    end = input("Wenn nicht, dann drücke n (no):   ").lower()

    if end == "y":
        end = 0
    elif end == "n":
        end = 1