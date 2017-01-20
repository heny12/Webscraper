""" Module provides helper methods for use in webscraper program """

# import regular expression module
import re

def list_to_line(lst):
    """ Converts a list to a single line string """
    return ''.join(lst)

def list_to_multi_line(lst):
    """ Converts a list to a multiple lined string with each element on a new line """
    return '\n'.join(lst)

def get_valid_words(text):
    """ Gets all words that consist of 2+ characters and have surrounding whitespace """
    valid_word_pattern = r"(?<=[ ])[a-zA-Z]{2,}(?=[ ]|$)"
    valid_words = re.findall(valid_word_pattern, ' ' + text)
    return valid_words

def word_sequences(words):
    """ Gets all sequences of 2+ consecutive title-case words from a given string """
    sequence_pattern = r"([A-Z][a-zA-Z]+(?=\s[A-Z])(?:\s[A-Z][a-zA-Z]+){1,})+"
    sequences = re.findall(sequence_pattern, words)
    return sequences
