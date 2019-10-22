'''
fuzzy.py

Lint this file using PyLint.
'''

# This function does some maths on three numbers.
def maths(input_a, input_b, input_c):
    ''' This function will multiply the first input by 3,
    then subtract the second and add the third inputs respectively.
    '''
    result = input_a * 3 - input_b + input_c
    return result

# This function returns True or False.
def choices(question):
    '''Makes sure a question is asked, will return True if so.'''
    return bool(question)

def main():
    '''Will execute both the previous functions.'''
    # first function takes three numbers
    answer = maths(3, 9, 2.3)
    print(answer)
    # second function takes a True or False
    new_answer = choices(True)
    print(new_answer)

if __name__ == '__main__':
    main()
