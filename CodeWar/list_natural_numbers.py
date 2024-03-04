def list_all_natural_numbers_under_given_number(number):
    return sum ([i for i in range(1, number) if i%3 ==0 or i%5 == 0 ])

def return_x_if_div3_or_y_if_div5_z_if_both(number):

    if number %3 == 0 and number %5 == 0:
        return 'z'
    elif number %3 == 0:
        return 'x'
    elif number %5 == 0:
        return 'y'


if __name__ == '__main__':
    print (list_all_natural_numbers_under_given_number(3))
    print (return_x_if_div3_or_y_if_div5_z_if_both(35))