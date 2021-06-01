def is_palindrome(input_string):
    new_string = " "
    old_string = " "
    input_string = input_string.lower()
    for x in input_string:
        if x!=" ":
            new_string = new_string+x
            old_string = x+old_string
    if new_string==old_string:
        return True
    return False
print(is_palindrome("never odd or even"))
print(is_palindrome("abcd"))
