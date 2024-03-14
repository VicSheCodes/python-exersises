"""
 Mastering `defaultdict` can greatly enhance your Python programming skills, especially when dealing with
 scenarios where you need to handle default values efficiently. Here are some exercises to help you practice using 
 `defaultdict`:

### Exercise 1: Word Frequency Counter
Write a Python program that takes a list of words as input and counts the frequency of each word. Use a `defaultdict`
 to store the word counts, with the default value initialized to 0.

### Exercise 2: Grouping Elements
Given a list of tuples representing (category, value) pairs, write a function that groups the values by category. Use 
a `defaultdict` to store the grouped values.

### Exercise 3: Graph Representation
Implement a simple graph data structure using a `defaultdict`. Write functions to add vertices and edges to the graph,
 as well as functions to retrieve the neighbors of a vertex and check if two vertices are adjacent.

### Exercise 4: Inverted Index
Write a program that builds an inverted index from a collection of documents. Given a list of (document_id, text)
tuples, create an inverted index where each word is mapped to a list of document IDs where it appears.
Use a `defaultdict` to store the inverted index.

### Exercise 5: Letter Frequency in Words
Given a list of words, write a program that calculates the frequency of each letter in the words. Use a `defaultdict`
to store the letter counts, with the default value initialized to an empty list.

### Exercise 6: Anagram Groups
Write a function that takes a list of words and groups them into sets of anagrams. Use a `defaultdict`
to store the anagram groups, with the default value initialized to an empty set.

### Exercise 7: Sparse Matrix
Implement a sparse matrix data structure using a nested `defaultdict`. Write functions to set and get values
in the matrix, as well as functions to iterate over the non-zero elements.

### Exercise 8: Multi-level Grouping
Given a list of tuples representing (category1, category2, value) triples, write a function that groups the values by
category1 and then by category2. Use a nested `defaultdict` to store the grouped values.

### Exercise 9: Trie Data Structure Implement a trie data structure for efficient prefix search. Use nested
`defaultdict` instances to represent the trie nodes.

### Exercise 10: URL Parsing
Write a function that parses a list of URLs and extracts the domain names and paths. Use a `defaultdict` to store the
parsed components, with the default value initialized to an empty string.

These exercises cover a variety of scenarios where `defaultdict` can be useful. Practice solving them to gain a 
deeper understanding of how to leverage `defaultdict` effectively in your Python projects. """
import os
from collections import defaultdict

file_path = os.path.join(os.getcwd(), "Data_files", "text_file.txt")


def word_frequency_counter(file_path):
    with open(file_path, 'r') as file:
        words = file.read().lower().split()
        print(type(words))
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        print(word_count)
    return word_count


def test_word_frequency_counter():
    print(f" \n Let's rock! ")
    word_frequency_counter(file_path)['a'] == 12


data = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot'), ('fruit', 'orange')]


def grouping_elements(list_of_tuples):
    sort_by_group = defaultdict(list)
    for category, value in list_of_tuples:
        sort_by_group[category].append(value)
    return sort_by_group


def test_grouping_elements():
    print(f" \n testing test_grouping_elements: ")
    assert grouping_elements(data) == {'fruit': ['apple', 'banana', 'orange'], 'vegetable': ['carrot']}
