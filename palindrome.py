def is_palindrome(s):
    return s == s[::-1]

def make_palindrome(s):
    rev_s = s[::-1]
    prefix = ""
    for i in range(len(s)):
        if is_palindrome(s[i:]):
            break
        prefix += s[i]
    return prefix + rev_s

input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("null")
else:
    palindrome_string = make_palindrome(input_string)
    print(f"To make a palindrome: {palindrome_string}")