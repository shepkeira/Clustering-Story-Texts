import os
import re
from file_access import *
from nltk.stem import PorterStemmer

## Preprocessing
# 1) convert everything to lowercase
# 2) removign all the stop-words (see stopwords.txt) and punctuations and non-word characters
# 3) applying the Porter stemming alorithm (there are various implementations depending on your language of choice)

# Stop words stored in a string
STOP_WORDS = read_file(os.path.join(os.getcwd(), "stopwords.txt"))

# Input: A string of the contents of a file
# Output: Preporcessed file contents: all lowercase, no stop words, no punctuation, no non-word characters, Porter stemming aloritm aplied
def process_contents(contents):
    lower_case_contents = contents.lower()
    only_needed_contents = remove_unneeded_contents(lower_case_contents)
    stemmed_contents = porter_stemmer_algorithm(only_needed_contents)
    process_contents = " ".join(stemmed_contents)
    return process_contents

# Input: A string of file contents
# Outout: An array of words excluding stop words, punctutaiton, non-word characters
def remove_unneeded_contents(contents):
    return_contents = []
    # split string into an array of words
    split_contents = re.split(' ', contents)
    for word in split_contents:
        #remove non-alphabetic characters
        return_word = ""
        for character in word:
            if character.isalpha():
                return_word += character
        #if word was all non-alphabetic characters we can move on
        if len(return_word) == 0:
            next
        #check it word with only alphabetic characters is a stop words; keep only non stop words
        if return_word not in STOP_WORDS:
            return_contents.append(return_word)
    return return_contents

# Input: array of words
# Output: array of words stemmed as much as possible according to Porter Stemming via nltk library
def porter_stemmer_algorithm(contents):
    ps = PorterStemmer()
    return_contents = []
    while True:
        for word in contents:
            return_contents.append(ps.stem(word))
        # stem untill no more stemming happens
        if return_contents == contents:
            break
        else:
            contents = return_contents
            return_contents = []
    return return_contents