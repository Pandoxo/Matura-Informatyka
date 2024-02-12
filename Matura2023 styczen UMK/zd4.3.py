file = open("slowa.txt", "r").read().split('\n')
output = open("rodziny.txt", "w")

def czy_palindrom(txt):
    for i in range(0, len(txt)):
        if txt[i] != txt[len(txt) - i - 1]:
            return False
    return True

palindromy = []
for word in file:
    if czy_palindrom(word):
        palindromy.append(word)


rodziny = []

for l in range(1,200):
    rodzina = []
    for pal in palindromy:
        if len(pal) == l:
            rodzina.append(pal)
    rodziny.append(sorted(rodzina))


for rodzina_ in rodziny:
    for pal_ in rodzina_:
        output.write(f"{pal_} ")
    output.write("\n")

