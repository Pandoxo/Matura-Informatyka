file = open("liczby.txt" , "r").read().split("\n")
wyniki = open("wyniki4.txt","a")

def reverse(txt):
    result = ""
    for i in range(len(txt)-1,-1,-1):
        result += txt[i]
    return result

for num in file:
    reflection = int(reverse(num))
    if reflection % 17 == 0:
        wyniki.write(f"{reflection}\n")
