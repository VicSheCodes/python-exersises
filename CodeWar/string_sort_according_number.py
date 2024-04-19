import re
from collections import OrderedDict


def order(sentence):
    if len(sentence) > 0:
        tmp_sentence = {}
        for word in sentence.split():
            num = int(re.search(r'\d+', word).group())
            tmp_sentence.update({num: word})

        ordered_sentence = dict(sorted(tmp_sentence.items()))
        for key, value in ordered_sentence.items():
            print(key, value)
        print(' '.join(map(str, ordered_sentence.values())))
    else:
        print("Empty")


if __name__ == '__main__':
    order("is2 Thi1s T4est 3a")
    order("")
