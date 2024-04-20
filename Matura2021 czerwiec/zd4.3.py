file = open("napisy.txt", "r").read().split("\n")
file.pop()


def palindrom(txt):
    if txt == txt[::-1]:
        return True
    return False

password = ""
for line in file:
    new_word = line + line[0]
    new_word2 = line[-1] + line
    if palindrom(new_word):
        password += new_word[25]
        continue
    if palindrom(new_word2):
        password += new_word2[25]
        continue

print(password)


