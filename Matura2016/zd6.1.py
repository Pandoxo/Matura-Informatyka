file = open("dane_6_1.txt", "r")
wyniki = open("wyniki_6_1.txt", "a")

def Cipher(word, key):
    result = ""
    for letter in word:
        move = ord(letter) + key % 26
        if move > 90:
            move -= 26
        result += chr(move)

    return result

for txt in file:
    wyniki.write(Cipher(txt,107))
