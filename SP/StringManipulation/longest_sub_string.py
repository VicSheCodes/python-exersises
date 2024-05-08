def find_longest_substring_without_repeating_characters(string):
    start = max_length = 0
    char_index_map = {}

    for i, char in enumerate(string):
        if char in char_index_map:
            start = max(start, char_index_map[char] + 1)
        char_index_map[char] = i
        length = i - start + 1
        if length > max_length:
            max_length = length
            longest_substring_start = start

    return max_length, string[longest_substring_start:longest_substring_start + max_length]

if __name__ == '__main__':
    a, b = find_longest_substring_without_repeating_characters("abcabcbb")
    print(a, b)
