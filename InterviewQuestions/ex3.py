'''

1. **Palindrome Checker**: Write a function to check if a given string is a palindrome.
The main approach is to compare the string with its reverse.

2. **FizzBuzz**: Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".

3. **Prime Number Checker**: Create a function to determine if a given number is prime or not.
The main approach involves checking divisibility by numbers up to the square root of the number.

4. **Factorial Calculator**: Write a function to calculate the factorial of a given number.
The main approach involves iterative or recursive multiplication.

5. **Anagram Checker**: Create a function to check if two strings are anagrams of each other.
The main approach involves sorting both strings and comparing them.

6. **Reverse a String**: Write a function to reverse a given string.
The main approach involves slicing or iterating through the string backwards.

7. **Count Vowels and Consonants**: Write a function to count the number of vowels and consonants in a given string.
The main approach involves iterating through the string and checking each character.

8. **Find the Largest Element in a List**: Write a function to find the largest element in a given list.
The main approach involves iterating through the list and keeping track of the largest element found so far.

9. **Check for Pangram**: Write a function to check if a given sentence is a pangram or not.
The main approach involves checking if all letters of the alphabet are present in the sentence.

10. **Calculate the Fibonacci Sequence**: Write a function to generate the Fibonacci sequence up to a specified number of terms.
The main approach involves iterative or recursive addition.

11. **Check for Armstrong Number**: Write a function to check if a given number is an Armstrong number or not.
The main approach involves decomposing the number into its digits and performing certain calculations.

12. **Check for Palindrome Number**: Write a function to check if a given number is a palindrome.
The main approach is similar to checking a palindrome string but involves number manipulation.

13. **Calculate the GCD (Greatest Common Divisor)**: Write a function to find the GCD of two numbers.
The main approach involves using Euclid's algorithm.

14. **Sort a List of Strings**: Write a function to sort a list of strings in alphabetical order.
The main approach involves using Python's built-in sorting functions.

15. **Check for Perfect Number**: Write a function to check if a given number is a perfect number or not.
The main approach involves finding the factors of the number and checking if their sum equals the number itself.

16. **Find the Second Largest Element in a List**: Write a function to find the second largest element in a given list.
The main approach involves finding the largest element first and then searching for the second largest.

17. **Binary to Decimal Converter**: Write a function to convert a binary number to its decimal equivalent.
The main approach involves iterating through the binary digits and performing the conversion.

18. **Decimal to Binary Converter**: Write a function to convert a decimal number to its binary equivalent.
The main approach involves repeated division by 2 and storing remainders.

19. **Check for Amicable Numbers**: Write a function to check if a pair of numbers are amicable or not.
The main approach involves finding the proper divisors of each number and checking if their sums equal each other.

20. **Check for Leap Year**: Write a function to check if a given year is a leap year or not.
The main approach involves checking if the year is divisible by 4, but not by 100 unless it is also divisible by 400.

'''


# Clause 1: Divisible by 4 but not by 100, and also not by 400
# year1 = 2008  # Divisible by 4, not by 100, not by 400 - Leap year
# year2 = 2016  # Divisible by 4, not by 100, not by 400 - Leap year
#
# # Clause 2: Divisible by 4, by 100, and by 400
# year3 = 2000  # Divisible by 4, by 100, by 400 - Leap year
# year4 = 2400  # Divisible by 4, by 100, by 400 - Leap year
#
# # Not Leap Years
# year5 = 1900  # Divisible by 4 and by 100, but not by 400 - Not a leap year
# year6 = 2100  # Divisible by 4 and by 100, but not by 400 - Not a leap year
# year7 = 1700  # Divisible by 4 and by 100, but not by 400 - Not a leap year


def is_a_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def test_leap_year():
    test_cases = {
        1900: False,  # Divisible by 100 but not by 400, not a leap year
        1996: True,  # Divisible by 4 but not by 100, leap year
        2000: True,  # Divisible by 400, leap year
        2004: True,  # Divisible by 4 but not by 100, leap year
        2100: False,  # Divisible by 100 but not by 400, not a leap year
        2400: True  # Divisible by 400, leap year
    }
    for year, expected_result in test_cases.items():
        assert is_a_leap_year(year) == expected_result, f"Failed for year {year}"


def amicable(num_a, num_b):
    proper_divisor = 1
    sum_of_proper_divisors_of_a = 0
    sum_of_proper_divisors_of_b = 0

    while proper_divisor < num_a:
        if num_a % proper_divisor == 0:
            sum_of_proper_divisors_of_a += proper_divisor
        proper_divisor += 1

    proper_divisor = 1
    while proper_divisor < num_b:
        if num_b % proper_divisor == 0:
            sum_of_proper_divisors_of_b += proper_divisor
        proper_divisor += 1

    return num_b == sum_of_proper_divisors_of_a and num_a == sum_of_proper_divisors_of_b


def amicable_2(num_a, num_b):
    sum_of_proper_divisors_a = sum(proper_divisor for proper_divisor in range(1, num_a) if num_a % proper_divisor == 0)
    sum_of_proper_divisors_b = sum(proper_divisor for proper_divisor in range(1, num_b) if num_b % proper_divisor == 0)
    return sum_of_proper_divisors_a == num_b and sum_of_proper_divisors_b == num_a


def test_amicable():
    num_a = 220
    num_b = 284
    assert amicable(num_a, num_b) == True, f"Failed for {num_a} and {num_b}"
    assert amicable_2(num_a, num_b) == True, f"Failed for {num_a} and {num_b}"


def decimal_to_binary_converter(num):
    if num == 0:
        return '0'
    binary_string = ''
    while num > 0:
        binary_string += str(num % 2)
        num = num // 2
    return binary_string[::-1]


def test_decimal_to_binary_converter():
    test_cases = {
        0: '0',
        1: '1',
        2: '10',
        5: '101',
        10: '1010',
        13: '1101',
        100: '1100100',
        255: '11111111',
        1024: '10000000000'
    }

    for decimal, expected_binary in test_cases.items():
        assert decimal_to_binary_converter(
            decimal) == expected_binary, \
            f"Failed for {decimal}. Expected: {expected_binary}, Actual: {decimal_to_binary_converter(decimal)} "


def binary_to_decimal_converter(binary_string):
    decimal = 0
    binary_string = binary_string[::-1]  # Reverse the binary string
    for i in range(len(binary_string)):
        decimal += int(binary_string[i]) * (2 ** i)
    return decimal


def test_binary_to_decimal_converter():
    test_cases = {
        '0': 0,
        '1': 1,
        '10': 2,
        '101': 5,
        '1010': 10,
        '1101': 13,
        '1100100': 100,
        '11111111': 255,
        '10000000000': 1024
    }

    for binary, expected_decimal in test_cases.items():
        assert binary_to_decimal_converter(binary) == expected_decimal, \
            f"Failed for {binary}. Expected: {expected_decimal}, Actual: {binary_to_decimal_converter(binary)} "


def find_second_largest(arr):


    if __name__ == '__main__':
        print(amicable(220, 284))
