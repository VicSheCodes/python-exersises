
def num_of_squares(numbers):
    return sum(num ** 2 for num in numbers)


if __name__ == "__main__":
   print( num_of_squares([1, 2, 2]))
