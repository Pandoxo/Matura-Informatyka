file = open("dane6.txt", "r").read().split("\n")
file.pop()


def check(num, p):
    contains_p_1 = False
    for integer in num:
        if int(integer) > p - 1:
            return 0
        if int(integer) == p - 1:
            contains_p_1 = True
    if contains_p_1:
        return True


def number_sum(num):
    result = 0
    for integer in num:
        result += int(integer)

    return result


for p in range(2, 11):
    count = 0
    biggest_sum = 0
    biggest_num = 0
    for num in file:
        if check(num, p):
            if number_sum(num) > biggest_sum:
                biggest_sum = number_sum(num)
                biggest_num = num

    print(p, biggest_num)
