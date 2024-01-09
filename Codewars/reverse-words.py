'''

Objective

Write a Function that, given a string parameter, reverses each word in the string and returns the string with every word reversed.

Constraints

All spaces in the given string should be retained.

''' 
def reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split(' '))