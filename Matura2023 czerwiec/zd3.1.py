file = open("anagram.txt", "r")
wyniki = open("wyniki3.txt", "a")

zrownowazone = 0
prawieZrownowazone = 0

for num in file:
    num = num[:-1]
    ones = 0
    zeros = 0
    for bit in num:
        if bit == "1":
            ones += 1
        else:
            zeros += 1
    if ones == zeros:
        zrownowazone += 1
    elif abs(ones - zeros) == 1:
        prawieZrownowazone += 1

wyniki.write(f'zrownowazone: {zrownowazone}\nprawiezrownowazone: {prawieZrownowazone}')


