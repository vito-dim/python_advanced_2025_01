class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


def pass_size_validation(passwd: str, min_size: int) -> bool:
    if len(passwd) < min_size:
        return False
    return True


def pass_common_validation(passwd: str, specials: set) -> bool:
    only_digits = passwd.isdigit()
    only_letters = passwd.isalpha()
    only_specials = all(char in specials for char in passwd)
    if only_letters or only_digits or only_specials:
        return False
    return True


def pass_special_validation(passwd: str, specials: set) -> bool:
    any_specials = any(char in specials for char in passwd)
    if not any_specials:
        return False
    return True


def pass_empty_validation(passwd: str) -> bool:
    if ' ' in passwd:
        return False
    return True


PASS_MIN_SIZE = 8
SPECIAL_SYMBOLS = {'@', '*', '&', '%'}

command = input()
while command != 'Done':
    current_password = command

    if not pass_size_validation(current_password, PASS_MIN_SIZE):
        raise PasswordTooShortError('Password must contain at least 8 characters')

    if not pass_common_validation(current_password, SPECIAL_SYMBOLS):
        raise PasswordTooCommonError('Password must be a combination of digits, letters, and special characters')

    if not pass_special_validation(current_password, SPECIAL_SYMBOLS):
        raise PasswordNoSpecialCharactersError('Password must contain at least 1 special character')

    if not pass_empty_validation(current_password):
        raise PasswordContainsSpacesError('Password must not contain empty spaces')

    print('Password is valid')

    command = input()
