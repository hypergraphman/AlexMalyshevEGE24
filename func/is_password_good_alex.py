def is_password_good(password):
    if len(password) < 8:
        return False
    if password.islower() or password.isupper() or password.isdigit():
        return False
    for i in '0123456789':
        if i in password:
            return True
    return False


print(is_password_good('adasfasdfaDSAFA232'))
print(is_password_good('34435345345232SDSDAFSDF'))
print(is_password_good('sadfsdfasdfSDSDAFSDF'))
print(is_password_good('adD232'))
print(is_password_good('adasfasdfa232'))
print(is_password_good('adasfasdfaDSAFA'))
print(is_password_good('ASDDSAFA232'))