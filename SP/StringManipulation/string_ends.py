
def is_suffix(word, suffix):
    return word.endswith(suffix)

def sum_of_squres(numbers):
    return sum(num ** 2 for num in numbers)

if __name__ == '__main__':
    print(is_suffix("hello", "o"))
    print(is_suffix("hello", "llo"))
    print(is_suffix("hello", "hello"))
    print(is_suffix("hello", ""))
    print(is_suffix("", ""))
    print(is_suffix("", "hello"))
    print(is_suffix("hello", "hell"))
    print(is_suffix("hell", "hello"))
    print(is_suffix("hell", "helloo"))
