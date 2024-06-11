
from collections import defaultdict


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pairs = 0
    socks_map = defaultdict(int)

    for num in ar:
        socks_map[num] += 1

    for num in socks_map.values():
        pairs += num // 2

    return pairs


if __name__ == '__main__':
    result = sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
    print(result)

