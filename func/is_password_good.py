from string import ascii_lowercase, ascii_uppercase, digits


def is_password_good(pswd):
    set_chars_pswd = set(pswd)
    return bool((len(pswd) >= 8 and set(ascii_uppercase) & set_chars_pswd and
           set(ascii_lowercase) & set_chars_pswd and set(digits) & set_chars_pswd))


print(is_password_good('adasfasdfaDSAFA232'))
print(is_password_good('adD232'))
print(is_password_good('adasfasdfa232'))
print(is_password_good('adasfasdfaDSAFA'))
print(is_password_good('ASDDSAFA232'))