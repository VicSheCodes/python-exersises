def list_all_natural_numbers_under_given_number(number):
    return sum ([i for i in range(1, number) if i%3 ==0 or i%5 == 0 ])


if __name__ == '__main__':
    print (list_all_natural_numbers_under_given_number(3))