def is_isogram(string):
    '''
        Casting the string into a set will drop the duplicate characters, causing isograms to return as True, 
        as the length of the set won't differ from the length of the original string:
    '''
    return len(set(string.lower())) == len(string)

m = 'moOse' 
if len(set(m.lower())) == len(m):
    print ('izogram')
else:
    print ('not izogram')

string = 'monday'

#shorter solution
is_isogram = lambda string: len(string) == len(set(string.lower()))

# import codewars_test as test
# from solution import is_isogram

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():      
#         test.assert_equals(is_isogram("Dermatoglyphics"), True )
#         test.assert_equals(is_isogram("isogram"), True )
#         test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )
#         test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case" )
#         test.assert_equals(is_isogram("isIsogram"), False )
#         test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram" )