num = 243567
res = 0


def sum(num) -> int:
    while num > 9:
        res = sum_digit(num)
        num = res
    return num


pass


def sum_digit(num) -> int:
    res = 0
    for i in range(len(str(num))):
        res += num % 10
    num = num / 10
    return res


print(sum(num))


