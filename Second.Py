def display_even_index_characters(input_string):
    even_index_characters = input_string[::2]
    return even_index_characters

# Get input from the user
user_input = input("Enter a string: ")

# Display characters at even index numbers
result = display_even_index_characters(user_input)
print("Characters at even index numbers:", result)