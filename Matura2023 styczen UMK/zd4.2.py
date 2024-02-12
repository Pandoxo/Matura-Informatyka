file = open("slowa.txt", "r").read().split('\n')


def czy_palindrom(txt):
    for i in range(0, len(txt)):
        if txt[i] != txt[len(txt) - i - 1]:
            return False
    return True


word_lenght_count = [0 for _ in range(200)]

for word in file:
    if czy_palindrom(word):
        word_lenght_count[len(word)] += 1

count = 0
for l in word_lenght_count:
    if l != 0:
        count +=1

print(count)