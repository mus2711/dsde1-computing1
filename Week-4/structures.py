'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list". 
def first_and_last(the_list):
    '''Will return first and last element of input.'''
    new_list = []
    new_list.append(the_list[0])
    new_list.append(the_list[-1])
    return new_list
    
# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception. 
def parameter_list(the_list, beginning, end):
    if beginning < end:
        new_list = the_list[beginning:end]
        new_list.reverse()
        return new_list
    else:
        return ValueError

# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    for x in range(2):
        the_list.insert(index, the_list[index])
    return the_list

# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    if word == word[::-1]:
        return True
    else: 
        return False
# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    import string
    valid = set(string.ascii_letters)
    sentence = sentence.lower()
    s = ''.join([x for x in sentence if x in valid])
    if s == s[::-1]:
        return 'Sentence is a palindrome.'
    else:
        return "Sentence is not a palindrome"

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentenece1, sentence2):
    sentenece1.lstrip()
    sentence2.lstrip()
    ns3 = sentenece1 + ' ' + sentence2
    new_list = ns3.split()
    if new_list[0][0].isupper():
        if new_list[-1][-1] in ['.','!','?']:
            final_sentence = ' '.join(new_list)
            return final_sentence
        else:
            return 'Please make sure that your clauses are gramatically correct.'

    else:
        return 'Please make sure that your clauses are gramatically correct.'

# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    if value in dictionary.values():
        return True
    else:
        return False

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    return dictionary1.update(dictionary2)