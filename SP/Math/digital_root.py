def digital_root(n):
    if -10 < n < 10:
        return n

    while n >= 10:
        sum = 0
        while n > 0:
            sum += n % 10
            n = n // 10
        n = sum
    return n


def digital_root2(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n


def digital_root3(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


if __name__ == "__main__":
    print(digital_root(15))
    print(digital_root3(10))
    print(digital_root2(1234))
    print(digital_root3(0))
    print(digital_root(123456789))
