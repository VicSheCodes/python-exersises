# In this example, after unpacking the elements from the generator into numbers_list, the generator
# generator is fully consumed. When we attempt to iterate over generator again in the for loop,
# it won't yield any more values because it has already been exhausted. As a result, the loop won't execute,
# which might not be the intended behavior.
#
# To avoid this problem, you can either avoid unpacking the generator if you need to iterate over
# it multiple times, or recreate the generator if you need to reuse it
def generate_numbers():
    yield 1
    yield 2
    yield 3


def test_generate_numbers():
    generator = generate_numbers()
    # Unpack the generator into a list
    numbers_list = [*generator]
    print(numbers_list)  # Output: [1, 2, 3]

