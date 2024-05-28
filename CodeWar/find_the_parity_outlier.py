'''
Use filter if you want to find all items in an array that meet a specific condition. 
Use find if you want to check if that at least one item meets a specific condition. 
Use includes if you want to check if an array contains a particular value. 
Use indexOf if you want to find the index of a particular item in an array.
'''

'''You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
'''
import unittest

arr1 = [2, 4, 0, 100, 4, 11, 2602, 36]
arr2 = [160, 3, 1719, 19, 11, 13, -21]

# returns True if number is even
def check_even(number):
    if number % 2 == 0:
          return number  
    return 0

# returns True if number is odd
def check_odd(number):
    if number % 2 == 1:
          return number  
    return 0

def find_outlier(integers):
    numbers_iterator = 0
    
    if integers[0]% 2 == integers[1]% 2:
        # find out is it array of odds or evens
        if integers[0]% 2 == 0 and list(filter(check_odd, integers)):
            return list(filter(check_odd, integers))[0]
        elif integers[0]% 2 == 1 and list(filter(check_even, integers)):
            return list(filter(check_even, integers))[0] 
    elif integers[0]% 2 != integers[1]% 2:
        if integers[2]%2 == 0 and list(filter(check_odd, integers)):  # most array is even
            return list(filter(check_odd, integers))[0]
        else:
            if list(filter(check_even, integers)) and list(filter(check_even, integers)):
                return list(filter(check_even, integers))[0] 
            
    return None



print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))

