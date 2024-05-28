"""
 examples of finding duplicate characters in a string, each emphasizing different aspects
such as readability, simplicity, runtime, memory efficiency, performance, use of collections,
built-in functions, etc
"""

from collections import Counter

SENTENCE = "You say goodbye and I say hello. Hello, hello. I don't know why "


def find_duplicate_characters_simple(string):
    """
        This implementation iterates through the string and uses a dictionary to
        count occurrences of each character. Then, it collects characters with
        counts greater than 1.
        When to Use: This approach is suitable when readability is a priority and
                     the input size is not very large.
        Strengths: Easy to understand and implement, suitable for small
                   to moderate input sizes.
        Weaknesses: Not the most efficient for larger input sizes due to
                    iterating through the string twice.

    Args:
        string:

    Returns:
        object:
    """
    char_counter = {}
    duplicates = []

    for char in string:
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1
    for char, count in char_counter.items():
        if count > 1:
            duplicates.append(char)

    return duplicates


def find_duplicates_using_collections(string):
    """
    When to Use: Use this approach when you want a concise and efficient solution without
                sacrificing readability.
    Strengths: Utilizes built-in Python functions for efficient counting and filtering,
                concise implementation.
    Weaknesses: May not be the most efficient for very large input sizes due to the
                overhead of creating a Counter object.
    Args:
        string:

    Returns:
        object:

    """
    counted_char = Counter(string)
    duplicates = [char for char in counted_char if counted_char[char] > 1]

    return duplicates


def find_duplicates_runtime(string):
    """
   Strengths:
    Efficiency: Achieves optimal runtime performance by using sets to track duplicate
    characters. It only requires a single pass through the string.
    Memory Efficiency: Requires less memory overhead compared to Approach 2 since
    it only maintains sets for seen characters and duplicates.
    Preservation of Ordering: Since it traverses the string sequentially, the
    order of duplicates is preserved.
    Weaknesses:

    Complexity: The implementation might be slightly more complex compared to using
    Counter, especially for those unfamiliar with set operations.
    Limited Reusability: While efficient for duplicate detection, the approach may not
     be as versatile for more complex string manipulation tasks.
     Not Suitable for All Operations: While efficient for finding duplicates,
     it may not be the best approach for tasks requiring more detailed chars counting or analysis.

    Args:
        string:

    Returns:

    """
    seen = set()
    duplicates = set()
    for char in string:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)

    return sorted(list(duplicates))


def find_duplicates_memory(string):
    seen = set()
    for char in string:
        if char in seen:
            yield char
        else:
            seen.add(char)


def find_duplicate_using_list_comprehension(string):
    return list(set(char for char in string if string.count(char) > 1))


if __name__ == '__main__':
    print("1 ", find_duplicate_characters_simple(SENTENCE))
    print("2 ", find_duplicates_using_collections(SENTENCE))
    print("3 ", find_duplicates_runtime(SENTENCE))
    print("4 ", list(find_duplicates_memory(SENTENCE)))
    print("5 ", find_duplicate_using_list_comprehension(SENTENCE))

    # for char in counted_char:
    #     if counted_char[char] > 1:
    #         yield char
