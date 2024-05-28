def count_bits(n)->int:
    count = 0
    for character in (str(bin(n))):
        if character == '1':
            count += 1
    
    return count

def count_bits2(n)->int:
    return m.bit_count()

def countBits(n):
    """ count_bits == PEP8, forced camelCase by CodeWars """
    return '{:b}'.format(n).count('1')

print (countBits(1234))

m=123456
print(count_bits2(m))
print((-m).bit_count())

# import codewars_test as test
# from solution import count_bits

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it("Basic Tests")
#     def basic_tests():
#         test.assert_equals(count_bits(0), 0)
#         test.assert_equals(count_bits(4), 1)
#         test.assert_equals(count_bits(7), 3)
#         test.assert_equals(count_bits(9), 2)
#         test.assert_equals(count_bits(10), 2)