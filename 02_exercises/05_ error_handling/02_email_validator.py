class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


MAIL_MIN_LENGTH = 5
VALID_DOMAINS = {'.com', '.bg', '.org', '.net'}
mail = input()

while mail != 'End':
    if '@' not in mail:
        raise MustContainAtSymbolError('Email must contain @')

    mail, domain = mail.split('@')
    if len(mail) < MAIL_MIN_LENGTH:
        raise NameTooShortError('Name must be more than 4 characters')

    domain_extension = f".{domain.split('.')[-1]}"
    if domain_extension not in VALID_DOMAINS:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    mail = input()
