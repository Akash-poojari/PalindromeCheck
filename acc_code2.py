def is_palindrome(string):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_string = ''.join(string.split()).lower()
    return cleaned_string == cleaned_string[::-1]

def make_palindrome(string):
    # Check if the string is already a palindrome
    if is_palindrome(string):
        print("null")
    else:
        # Find the longest palindromic suffix
        for i in range(len(string)):
            if is_palindrome(string[i:]):
                remaining = string[:i][::-1]
                print(remaining)
                break

# Input string
input_string = input("Enter a string: ")

# Call the function to check and print the result
make_palindrome(input_string)