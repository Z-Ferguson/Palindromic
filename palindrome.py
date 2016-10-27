import re

def is_palindrome(user_input):
#return True or False if the sentence is or isn't a palindrome
#takes a string and returns a boolean (True or False).
    pattern = '[^A-Za-z]'
    #cleans the string
    clean_user_input = re.sub(pattern, '', user_input)
    clean_user_input = clean_user_input.lower()
#makes input of a single letter true
    if len(clean_user_input) <= 1:
        return True
#if the beggining of the string is not equal to the end of the string, False.
    if clean_user_input[0] != clean_user_input[-1]:
        return False
#will take the next inputs from begging and end of string and compare
    return is_palindrome(clean_user_input[1:-1])

def main():
    user_input = input("Please provide a word or sentence: ")

    palindrome_verdict = is_palindrome(user_input)

    if palindrome_verdict:
        print('That is a palindrome!')
    else:
        print('That is not a palindrome!')

if __name__ == '__main__':
    main()
