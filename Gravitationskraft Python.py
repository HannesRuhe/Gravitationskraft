# Gravitationskraft:
#
# Variabeln: F = Gravitationskraft = graviKra
#            Fg = Gewichtskraft = gewiKra
#            G = Gravitationskonstante = graviKo
#            Ge = Gravitationskonstante Erde = graviKoE
#            m1 = Masse 1 in Kg = mass1
#            m2 = Masse 2 in Kg = mass2
#            r² = Abstand der Massen hoch 2 = abstand
#
# Zwei Massen: F = G * (m1 * m2) / r²
# Erde:        Fe = Ge * m1

# Texte:

einführung = """
    Hallo, hast du lust die Anziehung
    zwischen zwei Objekten zu berechnen,
    oder die Gewichtskraft von einem
    Körper zur Erde?
    
    Sicher nicht ...
    
    Deswegen hilft dir dieses Program die
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

import time # Zeitverzögerung aktivieren
print("...")
time.sleep(1) # Zeitverzögerung für 2 Sekunden anwenden
print("...")
time.sleep(1)
print("...")
time.sleep(1)

# Rechenart definieren:

rechenart1 = input(rechenarttext1)

if rechenart1 == "y":
    
# Variabeln definieren:

    mass1 = float(input("Gib die Masse in Kg von deinem ersten Objekt an: "))
    mass2 = float(input("Gib die Masse in Kg von deinem zweiten Objekt an: "))
    abstand = float(input("Gib den Abstand deiner Objekte in Meter an: "))
    
# Berechnungen durchführen:
    
    rechenschritt1 = mass1 * mass2
    rechenschritt2 = rechenschritt1 / abstand
    graviKra = rechenschritt2 * 6.67e-11
    
    # Ausgabe:
    print("Die Anziehungskraft in Newton beträgt", graviKra)
    print("Das e in deiner Zahl steht für ~ hoch ~")
    
    
elif rechenart1 == "n":
    
# Rechenart definieren:
    
    rechenart2 = input(rechenarttext2)
    
    if rechenart2 == "y":
        
# Variabeln definieren:
    
        mass1 = float(input("Gib die Masse in Kg von deinem Objekt an: "))
    
# Berechnungen durchführen

        gewiKra = 9.81 * mass1
        
        # Ausgabe
        print("Die Gewichtskraft in Newton beträgt", gewiKra)
        
        
