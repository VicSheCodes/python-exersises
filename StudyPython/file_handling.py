# file handling
# read text file and count the occurrences of each word
import os
import time


def run_time_counter(func):
    def wrapper(file_path, *args, **kwargs):
        time_start = time.perf_counter()
        result = func(file_path)
        time_end = time.perf_counter()
        print(f"The {func.__qualname__} took {time_end - time_start:.5f} seconds to run")
        return result

    return wrapper


def count_function_executions(func):
    def wrapper(*args, **kwargs):
        wrapper.executions += 1
        print(f" \nFunction {func.__qualname__} has been called {wrapper.executions} times")
        return func(*args, **kwargs)

    wrapper.executions = 0
    return wrapper


def get_first_line(file_path):
    with open(file_path, 'r') as file:
        return file.readline()


@run_time_counter
@count_function_executions
def count_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().lower().split()
        word_count = {word: words.count(word) for word in words}
    return word_count


@run_time_counter
@count_function_executions
def count_words_2(file_path):
    with open(file_path, 'r') as file:
        word_count = {}
        for word in file.read().lower().split():
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count


@run_time_counter
@count_function_executions
def count_words_3(file_path):
    with open(file_path, 'r') as file:
        word_count = {}
        for word in file.read().lower().split():
            word_count[word] = word_count.get(word, 0) + 1

    return word_count


def test_count_words():
    print(f" \n Let's rock! ")
    print(f" \n File path is: ", path := os.path.join(os.getcwd(), "Data_files", "text_file.txt"), end="\n")
    counted_words = {
        "version 1": count_words(path),
        "version 2": count_words_2(path),
        "version 3": count_words_3(path)
    }
    for key, value in counted_words.items():
        print(f" \nThe words count using {key}: {value}")
        expected_hotel_word_count = 5
        assert counted_words[key]['hotel'] == expected_hotel_word_count, f"Assertion failed: Expected 'hotel' count " \
                                                                         f"to be {expected_hotel_word_count}, " \
                                                                         f"but got {counted_words['hotel']} "
        print(f" Assertion succeeded: The word 'hotel' appears {expected_hotel_word_count} times, as expected. \n")


# Counting Lines, Words, and Characters

def counting_lines_words_characters(file_path):
    with open(file_path, 'r') as file:
        file_lines = file.readlines()
        file_words = {word for lines in file_lines for word in lines.split()}
        file_characters = {char for lines in file_lines for char in lines}
    return file_lines, file_words, file_characters


