import string
import argparse

# Exercise 1
def char_freq(word:str):
    """
    -takes a string as its only argument
    -returns a dictionary:
        the keys of the dictionary are the letters that appear in the string
        for each letter, the associated value in the dictionary is the number of occurrences of the letter in the string
    """
    word_dictionary = {}
    
    for letter in word:
        if letter in word_dictionary:
            word_dictionary[letter] += 1
        else:
            word_dictionary[letter] = 1
    
    return word_dictionary

#Exercise 2 
def letter_freq(word:str):
    """
    -remove spaces
    -remove punctuation
    -count uppercase and lowercase letters together, but return lowercase letters in the result
    -it must use the char_freq function
    """

    # clean_txt = ''.join(ch for ch in word if ch not in string.punctuation).replace(" ", "")
    
    clean_txt = ""
    for l in word:
        lower_l = l.lower()
        if lower_l not in string.punctuation and lower_l != " ":
            clean_txt += lower_l

    clean_freq = char_freq(clean_txt)
    return clean_freq

#Exercise 3 
def histogram(clean_freq:str):
    """
    -This function return a multi-line list of all letters in a string
    with as many "*" characters as the number of times that letter appears in the string. 
    -You must use the output from letter_freq
    """
    result = []
    for letter in clean_freq:
        if letter in clean_freq:
            result.append(f"{letter}: {'*' * clean_freq[letter]}")
        
    return "\n".join(result)

#Exercise 4 
def main():
    """
    Takes a positional argument in_string - the string to process
    Provides three mutually exclusive optional flags:
        -c or --chars: Use the char_freq function
        -l or --letters: Use the letter_freq function
        -g or --histogram: Use the histogram function (default if no flag specified)
    The program should print the input string and the result of the selected operation.
    """

    parser = argparse.ArgumentParser(description='Analyze character frequency in a string')
    
    parser.add_argument('in_string', type=str, help='The string to process')
    
    operation = parser.add_mutually_exclusive_group()

    operation.add_argument('-c', '--chars', action='store_true', 
                      help='Use the char_freq function')
    operation.add_argument('-l', '--letters', action='store_true', 
                      help='Use the letter_freq function')
    operation.add_argument('-g', '--histogram', action='store_true', 
                      help='Use the histogram function (default)')
    
    args = parser.parse_args()

    result = None
    
    print(f"Input string: {args.in_string}\n")
    
    if args.chars:
        result = char_freq(args.in_string)
        operation_name = "Character frequency"
    elif args.letters:
        result = letter_freq(args.in_string)
        operation_name = "Letter frequency"
    elif args.histogram:
        freq = letter_freq(args.in_string)
        result = histogram(freq)
        operation_name = "Histogram"  
    else:
        result = args.in_string
        operation_name = "No operation"

    print(f"Input: '{args.in_string}'")
    print(f"Operation: {operation_name}")
    print(f"Result: '{result}'")

if __name__ == "__main__":
    main()

"""
word = "Testing Stuff!"
parsed = letter_freq(word)
if __name__ == "__main__":
    print(parsed)
    print(histogram(parsed))
"""
    

