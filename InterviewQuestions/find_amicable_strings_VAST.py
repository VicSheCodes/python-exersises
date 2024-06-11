from collections import defaultdict


def find_amicable_pairs_strings(words):
    # Step 1: Normalize the strings by sorting characters
    normalized_map = defaultdict(list)

    for string in words:
        key = ''.join(sorted(string))
        normalized_map[key].append(string)

    # Step 2: Extract amicable pairs
    # amicable_pairs = []
    # for key, group in normalized_map.items():
    #     if len(group) > 1:
    #         amicable_pairs.extend(group)

    amicable_pairs = [group for group in normalized_map.values() if len(group) > 1]

    return amicable_pairs


if __name__ == '__main__':
    strings = ["listen", "silent", "enlist", "google", "gogole", "abcd", "bcda", "cabd"]
    amicable_strings = find_amicable_pairs_strings(strings)
    print(amicable_strings)
