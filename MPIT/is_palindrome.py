def is_palindrome(string):
    return string == string[::-1]


def upgrade_is_palindrome(string):
    upgraded_string = ""
    for symbol in string.lower():
        if symbol.isalpha():
            upgraded_string += symbol
    return upgraded_string == upgraded_string[::-1]


def regular_is_palindrome(string):
    import re
    upgraded_string = "".join(re.findall(r'[a-z]+', string.lower()))
    return upgraded_string == upgraded_string[::-1]