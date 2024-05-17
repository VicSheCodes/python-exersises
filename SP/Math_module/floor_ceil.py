from math import floor, ceil


def get_floor_and_ceil(num):
    print(num // 10, num % 10)
    print(divmod(num, 7))
    print(floor(num), ceil(num))


start = 1
stop = 10
step = 2


def get_in_range(start, stop, step):
    # Calculate the division and integer division for each number in the range
    for num in range(start, stop, step):
        division, remainder = divmod(num, 3)
        print(f"{num} divided by 3: {division} with remainder {remainder}")


if __name__ == "__main__":
    get_floor_and_ceil(120)
    get_in_range(3, 20, 4)

