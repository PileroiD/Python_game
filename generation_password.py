import random

sumbols = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM' \
          '!@#$%^&*()_+|-=\\/<>/?:;"\'{}[]~'


def password(sumbol, ln):
    result = []
    for _ in range(ln):
        result.append(random.choice(list(sumbol)))
    return ''.join(result)


print(password(sumbols, 10))
