"""

Policies
~~~~~~~~

Contains Username_Policy, Password_Policy, and Character_Policy to verify if usernames and password strings pass given rules

Returns a string Good or an error string

Character_Policy returns True or False

"""

GOOD = "Good"

# XXX: the whole returning strings may be a terrible idea

def Username_Policy(username):

    if type(username) is not bytes:
        return "Bad username"

    # check username len is at least 5
    if len(username) < 5:
        return "Username length less than 5"

    return "Good"


def Password_Policy(password):

    if type(password) is not bytes:
        return "Bad password"

    # check if password is at least len 5
    if len(password) < 5:
        return "Password length less than 5"

    # One capital, one number, and one special
    if Character_Policy(password) is False:
        return "Password does not follow policy: one capital, one number, and one special character"

    return "Good"


def Character_Policy(byte_string):

    if type(byte_string) is not bytes:
        return False

    # One capital, one number, and one special
    has_special, has_number, has_upper = 0, 0, 0

    for byte in byte_string:

        # specials
        if byte in range(33, 48):
            has_special += 1
        # numbers
        if byte in range(48, 58):
            has_number += 1
        # uppers
        if byte in range(65, 91):
            has_upper += 1

        if has_special and has_number and has_upper:
            return True

    return False
