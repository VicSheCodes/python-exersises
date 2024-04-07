"""

Sure! Here are some Python exercises that you can try:

Fibonacci Sequence: Write a function to generate the Fibonacci sequence up to a certain number of terms.

Palindrome Checker: Write a function that checks if a given string is a palindrome (reads the same forwards
and backwards).

Factorial Calculator: Write a function to calculate the factorial of a given number.

Prime Number Checker: Write a function that checks if a given number is prime.

Reverse a String: Write a function that reverses a given string.

Word Count: Write a function that counts the occurrences of each word in a given string.

Sum of Squares: Write a function that calculates the sum of squares of a list of numbers.

Anagram Checker: Write a function that checks if two given strings are anagrams of each other.

FizzBuzz: Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz"
instead of the number, and for the multiples of five, print "Buzz". For numbers that are multiples of both
three and five, print "FizzBuzz".

Temperature Converter: Write functions to convert temperatures between Celsius and Fahrenheit.

"""

def fib(n):
    lst = [0, 1]
    if n <= 0:
        print(f" Invalid input")
    elif n == 1:
        print(f" [{lst[0]}]")
    elif n == 2:
        print(f" {lst}")
    else:
        while lst[-1] < n:
            lst.append(lst[-1] + lst[-2])
        print(f" {lst}")


def sum_fib(n):
    lst = [0, 1]
    if n <= 0:
        print(f" Invalid input")
    elif n == 1:
        print(f" {lst[0]}")
    elif n == 2:
        print(f" {lst[1]}")
    else:
        while lst[-1] < n:
            lst.append(lst[-1] + lst[-2])
        print(f" {lst}")
    print(f" the sum is : {sum(lst)}")


def factorial(n):
    product = n
    if n < 0:
        print(f" Invalid input.")
    elif n <= 1:
        print("1")
    else:
        while n > 1:
            n = n - 1
            product = product * n
        print(product)


# 1,2,3,5,7
def is_prime(n):
    m = n
    if n <= 1:
        print(f"{n} is not a prime number.")
        return False
    elif n <= 3:
        print(f"{n} is a prime number.")
        return True
    else:
        for m in range(2, n):
            if n % m == 0:
                print(f"{n} is not a prime number.")
                return False
            else:
                m = m - 1
        print(f"{n} is a prime number.")
        return True


if __name__ == "__main__":
    # sum_fib(1)
    # sum_fib(2)
    # sum_fib(6)

    # factorial(0)
    # factorial(1)
    # factorial(2)
    # factorial(3)
    # factorial(5)

    is_prime(0)
    is_prime(1)
    is_prime(2)
    is_prime(3)
    is_prime(4)
    is_prime(5)
    is_prime(6)
    is_prime(7)
    is_prime(8)
    is_prime(9)
    is_prime(10)
    is_prime(11)
