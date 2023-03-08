print("Tic-Tac-Toe Game in Python")

from os import system, name
spiel_aktiv = True
spieler_aktuell = "X"

spielfeld = ["",
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9"]

def clear():
    if name == "nt":
        _ = system('cls')

def spielfeld_ausgeben():
    print(spielfeld[1] + "|" + spielfeld[2] + "|" + spielfeld[3])
    print(spielfeld[4] + "|" + spielfeld[5] + "|" + spielfeld[6])
    print(spielfeld[7] + "|" + spielfeld[8] + "|" + spielfeld[9])

def spieler_eingabe():
    global spiel_aktiv
    while True:
        spielzug = input("Bitte Feld eingeben: ")
        #abbruch
        if spielzug == "q":
            spiel_aktiv = False
            return
        try:
            spielzug = int(spielzug)
        except ValueError:
            print("Bitte Zahl zwischen 1 bis 9 eingeben")
        else:
            if spielzug >= 1 and spielzug <= 9:
                if spielfeld[spielzug] == "X" or spielfeld[spielzug] == "O":
                    print("Das Feld ist bereits belegt - ein anderes muss gewählt werden")
                else:
                    return spielzug
            else:
                    print("Zahl muss zwischen 1 und 9 lieben")

def spieler_wechsel():
    global spieler_aktuell
    if spieler_aktuell == "X":
        spieler_aktuell = "O"
    else:
        spieler_aktuell = "X"

def kontrolle_gewonnen():
    #von links nach rechts
    if spielfeld[1] == spielfeld[2] == spielfeld[3]:
        return spielfeld[1]
    if spielfeld[4] == spielfeld[5] == spielfeld[6]:
        return spielfeld[4]
    if spielfeld[7]== spielfeld[8] == spielfeld[9]:
        return spielfeld[7]
    #von oben nach unten
    if spielfeld[1] == spielfeld[4] == spielfeld[7]:
        return spielfeld[1]
    if spielfeld[2] == spielfeld[5] == spielfeld[8]:
        return spielfeld[2]
    if spielfeld[3] == spielfeld[6] == spielfeld[9]:
        return spielfeld[3]
    #Diagonal
    if spielfeld[1] == spielfeld[5] == spielfeld[9]:
        return spielfeld[5]
    if spielfeld[3] == spielfeld[5] == spielfeld[7]:
        return spielfeld[5]

def kontrolle_unentschieden():
    if(spielfeld[1] == "X" or spielfeld[1 == "O"]) \
        and (spielfeld[2] == "X" or spielfeld[2] == "0") \
        and (spielfeld[3] == "X" or spielfeld[3] == "0") \
        and (spielfeld[4] == "X" or spielfeld[4] == "0") \
        and (spielfeld[5] == "X" or spielfeld[5] == "0") \
        and (spielfeld[6] == "X" or spielfeld[6] == "0") \
        and (spielfeld[7] == "X" or spielfeld[7] == "0") \
        and (spielfeld[8] == "X" or spielfeld[8] == "0") \
        and (spielfeld[9] == "X" or spielfeld[9] == "0"):
            return("Unentschieden")

#Hauptroutine 
spielfeld_ausgeben()
while spiel_aktiv:
    print()
    print("Spieler " + spieler_aktuell + " am Zug")
    spielzug = spieler_eingabe()
    if spielzug:
        spielfeld[spielzug] = spieler_aktuell
        clear()
        spielfeld_ausgeben()
        gewonnen = kontrolle_gewonnen()
        if gewonnen:
            print("Spieler " + gewonnen + " hat gewonnen!")
            spiel_aktiv = False
            break
        unentschieden = kontrolle_unentschieden()
        if unentschieden:
            print("Spiel ist unentschieden")
            spiel_aktiv = False
        spieler_wechsel()
print()