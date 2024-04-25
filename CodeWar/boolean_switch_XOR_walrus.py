'''
Create a function that always returns True/true for every item in a given list.
However, if an element is the word 'flick', switch to always returning the opposite boolean value.

Examples
['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]
'''


def flick_switch_1(lst):
    flag = True
    return [flag := not flag if word == 'flick' else flag for word in lst]


# Using XOR ^ that assighn evaluated value of expression
# flag ^ (word == 'flick') toggles the value of flag using bitwise XOR (^).
# If word is 'flick', it flips the value of flag, otherwise, it keeps the current value.
# The expression flag := flag ^ (word == 'flick') assigns the toggled value back to flag
def flick_switch_2(lst):
    flag = True
    return [flag := flag ^ (word == 'flick') for word in lst]


# Using zip to combine original list with list of True values
def flick_switch_3(lst):
    return [flag := not flag if word == 'flick' else flag for flag, word in zip([True], lst)]

