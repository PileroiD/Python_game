import random

sumbols = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM' \
          '!@#$%^&*()_+|-=\\/<>/?:;"\'{}[]~'


def password2(sumbol: str, lens: int):
    while True:
        result = []
        for _ in range(lens):
            result.append(random.choice(list(sumbol)))
        result = ''.join(result)
        print(f'\n{result}\n')
        q = input('Again?[y/n]')
        if q == 'y':
            continue
        else:
            break


n = int(input("Введите количество символов в пароле:"))
password2(sumbols, n)
