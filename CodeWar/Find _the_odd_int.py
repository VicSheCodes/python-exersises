import functools
import operator


def find_it(seq) -> int:
    # reduce - apply a particular function passed in its argument to all of the list elements 
    # mentioned in the sequence
    # xor - a logical operator which results true when either of the operands are true 
    # (one is true and the other one is false) but both are not true and both are not false
    return functools.reduce( operator.xor, seq ) 