file = open("przyklad.txt", "r")
wyniki = open("wyniki4.txt", "a")

maxCount = 0
maxWord = ""

for word in file:
    wordSorted = sorted(word[:-1])
    count = 1
    for i in range(0,len(wordSorted)-1):
        if wordSorted[i] != wordSorted[i+1]:
            count += 1
    if count > maxCount:
        maxCount = count
        maxWord = word[:-1]

wyniki.write(f'{maxWord} {maxCount}')
