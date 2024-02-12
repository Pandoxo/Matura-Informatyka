file = open("slowa.txt", "r").read().split('\n')

def czy_palindrom(txt):
    for i in range(0,len(txt)):
        if txt[i] != txt[len(txt) - i - 1]:
            return False
    return True

count = 0
for word in file:
    if czy_palindrom(word):
        count += 1

print(count)