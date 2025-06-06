def give_me_some_space(text):
    """Returns the text with spaces between each character."""
    return ' '.join(text)

# Example usage
user_input = input("Enter a word or sentence: ")
spaced = give_me_some_space(user_input)
print("With space:", spaced)
