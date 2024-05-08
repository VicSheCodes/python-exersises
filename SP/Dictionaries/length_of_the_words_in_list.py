
def lenght_of_the_words_in_the_list(list_of_words):
    word_lenght = {}
    for word in list_of_words:
        word_lenght[word] = len(word)
    yield word_lenght


def keep_words_length_in_dictionary(list_of_words):
    word_lenght = {}
    for word in list_of_words:
        word_lenght[word] = len(word)
    return word_lenght


def test_keep_words_length_in_dictionary():
    print(keep_words_length_in_dictionary(["Alice", "in", "Wonderland"]))
    print(*(lenght_of_the_words_in_the_list(["Gone", "with", "the", "wind"])))
