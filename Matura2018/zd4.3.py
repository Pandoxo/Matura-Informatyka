file = open("sygnaly.txt", "r")
wyniki = open("wyniki4.txt", "a")

for word in file:
    wordSorted = sorted(word[:-1])
    if abs(ord(wordSorted[0]) - ord(wordSorted[-1])) < 11:
        wyniki.write(f'{word[:-1]}\n')
