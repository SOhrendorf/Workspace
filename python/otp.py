import os
from tkinter import *

filename = input("Dateiname? ")
aktion = input("welche Aktion ausführen (verschlüsseln / entschlüsseln)? ")

def start(aktion):
    if aktion == "verschlüsseln":
        encrypt(filename)
    elif aktion == "entschlüsseln":
        decrypt(filename, filename + ".key")
    else:
        print("Keine gültige Aktion ausgewählt!")

def encrypt(filename):
    to_encrypt = open(filename, "rb").read()
    size = len(to_encrypt)
    key = os.urandom(size)
    with open(filename + ".key", "wb") as key_out:
        key_out.write(key)
    encrypted = bytes(a ^ b for (a, b) in zip(to_encrypt, key))
    with open(filename, "wb") as encrypted_out:
        encrypted_out.write(encrypted)

def decrypt(filename, key):
    file = open(filename, "rb").read()
    key = open(key, "rb").read()
    decrypted = bytes(a ^ b for (a, b) in zip(file, key))
    with open(filename, "wb") as decrypted_out:
        decrypted_out.write(decrypted)
    os.remove(filename + ".key")

#encrypt(filename)
#decrypt(filename, filename + ".key")
start(aktion)