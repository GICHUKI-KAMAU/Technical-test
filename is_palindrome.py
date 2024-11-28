def is_palindrome(input_str):
    # Removing the space and coonvert the string to lowercase
    cleaned_str = ''.join(e.lower() for e in input_str if e.isalnum())
    
    return cleaned_str == cleaned_str[::-1]

test_cases = [
    "madam",              #  True
    "racecar",            #  True
    "kayak",              #  True
    "nurses run",         #   True 
    "hello",              #  False
    "A man a plan a canal Panama",  # True
    "Was it a car or a cat I saw",  # True
    "not a palindrome",   #False
]

for phrase in test_cases:
    result = is_palindrome(phrase)
    print(f"'{phrase}' is a palindrome: {result}")
