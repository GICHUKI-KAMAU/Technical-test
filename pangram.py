
# Write a Python function to check whether a string is pangram or not. (Assume
# the string passed in does not have any punctuation)
def is_pangram(input_str):
    input_str = input_str.lower()
    
    # Creating a set of all the letters in the string
    letter_set = set(c for c in input_str if c.isalpha())
    
    return len(letter_set) == 26

# Testing different sentences
test_cases = [
    "The quick brown fox jumps over the lazy dog",  #  True 
    "Pack my box with five dozen liquor jugs",      # True
    "Hello world",                                  #  False
    "abcdefghijklmnopqrstuvwxyz",                     # True
    "The lazy dog jumped over the fence",           # False
]


for phrase in test_cases:
    result = is_pangram(phrase)
    print(f"'{phrase}' is a pangram: {result}")
