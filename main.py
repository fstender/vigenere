def menue():
    print()
    print("1. Verschlüsseln")
    print("2. Entschlüsseln")
    print("3. Ende")
    return input("> ")


def vigenere(eingabe, schluessel, verschluesseln):
    z = 0
    keyText = ''
    outputText = ''
    for c in eingabe:
        if c == ' ':
            keyText += ' '
            outputText += ' '
            continue

        k = schluessel[z]
        keyText += k
        if verschluesseln == True:
            d = ord(c) + ord(k) - 65
            if d > ord('Z'):
                d -= 26
        else:
            d = ord(c) - ord(k) + 65
            if d < ord('A'):
                d += 26
        outputText += chr(d)

        z += 1
        if z >= len(schluessel):
            z = 0
    return outputText, keyText


def verschluesseln():
    schluessel = str.upper(input("Schlüssel: "))
    klartext = str.upper(input("Klartext: "))

    codeText, schluesselText = vigenere(klartext, schluessel, True)    
    print()
    print('Klartext: ', klartext)
    print('Schlüssel:', schluesselText)
    print('Code:     ', codeText)


def entschluesseln():
    schluessel = str.upper(input("Schlüssel: "))
    code = str.upper(input("Code: "))

    klartext, schluesselText = vigenere(code, schluessel, False)
    print()
    print('Code:     ', code)
    print('Schlüssel:', schluesselText)
    print('Klartext: ', klartext)


while True:
    wahl = menue()
    if (wahl == "1"):
        verschluesseln()
    elif (wahl == "2"):
        entschluesseln()
    elif (wahl == "3"):
        break
