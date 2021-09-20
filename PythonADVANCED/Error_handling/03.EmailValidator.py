from Custom_errors import InvalidDomainError, NameTooShortError, MustContainAtSymbolError


def email_validation(email):
    try:
        name,domain = email.split('@')
    except ValueError:
        raise MustContainAtSymbolError ("Email must contain @")

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    try:
        domain_name, domain_end = domain.split('.')
        if domain_end not in ['org', 'com', 'bg', 'net']:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    except ValueError:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    return True


current_email = input()

while not current_email == 'End':
    if email_validation(current_email):
        print('Email is valid')
    current_email = input()

