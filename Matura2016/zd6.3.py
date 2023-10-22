file = open("dane_6_3.txt", "r")
wyniki = open("wyniki_6_3.txt", "a")


def Cipher(word, key):
    result = ""
    for letter in word:
        move = ord(letter) + key % 26
        if move > 90:
            move -= 26
        result += chr(move)

    return result


def good(words):

    for k in range(0, 26):
        if Cipher(words[0], k) == words[1]:
            return True
    return False


for txt in file:
    if not good(txt.split()):
        wyniki.write(txt.split()[0] + "\n")


