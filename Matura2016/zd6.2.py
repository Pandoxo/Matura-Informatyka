file = open("dane_6_2.txt", "r")
wyniki = open("wyniki_6_2.txt", "a")

def Decipher(word, key):
    result = ""
    for letter in word:
        move = ord(letter) - key % 26
        if move < 65:
            move += 26
        result += chr(move)

    return result

for txt in file:
    print(Decipher(txt.split()[0], int(txt.split()[1])))

#Zadanie jest dobrze zrobione tylko ta matura miala bledy w danych
