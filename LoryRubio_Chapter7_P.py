# Lory Rubio Programming Assignment 7
# This code has functions  that will allow the user to enter a paragraph, including sentences which begin with numbers.
# It will also display each individual sentence and the count of sentences in the paragraph.

# Import the module for re
import re

# Create function that will count the number of sentences in the paragraph by checking with set pattern.
def count(sentences):

    # Pattern that checks for the endings of a sentence.
    pat = r'.*?[.?!]'

    # Checks for matches of regex pattern and stores in lists of strings
    lst = re.findall (pat,sentences,flags=re.DOTALL )
    print('There are', len(lst), 'sentences,')

def individual(sentences):

    # Pattern that checks for sentences staring with a number or a capital letter until it ends with a .!?
    pat = r'(\d+[^.!?]*[.!?]|\s*[A-Z][^.!?]*[.!?])'

    # Stores the individual sentences that match the regex pattern
    m= re.findall(pat,sentences, flags=re.DOTALL | re.MULTILINE)

    # Loop that checks each sentence one at a time in list  and prints out the sentence
    for i in m:
        print ('->', i.strip())

# Defines main function that prints out the result  and calls the other functions.
def main ():
    sentences = input('Please enter your paragraph: ')
    count(sentences)
    individual(sentences)

# Call back main function
main()
