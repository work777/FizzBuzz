secret_number=25
x=0
anzahl=0


for anzahl in range (5):

    zaehler=4-anzahl

    x = int (raw_input("Geben Sie eine Zahl zwischen 1 und 50 ein: "))

    if x == 25:
        print "Sie haben die Zahl erraten, Gratulation!"
        break
    elif x < secret_number:
        print "Leider falsch. Sie muessen eine groessere Zahl eingeben!"
    elif x > secret_number:
        print "Leider falsch. Sie muessen eine kleinere Zahl eingeben!"

    if zaehler != 1:
        print "Sie haben noch", zaehler, "Versuche."
    else: print "Sie haben noch", zaehler, "Versuch."

    if zaehler == 0:
        print "Game over!"
