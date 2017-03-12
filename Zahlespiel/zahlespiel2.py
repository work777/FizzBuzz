secret_number = 25
x=0

while x != secret_number:
    x = int (raw_input("Geben Sie eine Zahl zwischen 1 und 50 ein"))

    if x == 25:
        print "Sie haben die Zahl erraten, Gratulation!"
        break
    elif x < secret_number:
        print "Leider falsch. Sie muessen eine groessere Zahl eingeben!"
    elif x > secret_number:
        print "Leider falsch. Sie muessen eine kleinere Zahl eingeben!"