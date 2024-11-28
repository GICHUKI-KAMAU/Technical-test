def capitalize_words(input_str):
    # Spliting the string into words, capitalizing each word, and joining them back together
    return ' '.join([word.capitalize() for word in input_str.split()])

test_cases = [
    "hi",                        # "Hi"
    "i love programming",         # "I Love Programming"
    "hello world",                # "Hello World"
    
]

# Testing the function on different sentences
for phrase in test_cases:
    result = capitalize_words(phrase)
    print(f"Input: '{phrase}' -> Capitalized: '{result}'")