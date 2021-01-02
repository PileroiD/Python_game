import itertools


def opn(path):
    with open(path, encoding='utf8') as file:
        new_file = file.read()
    new_file = new_file.split()
    return new_file


def sort(string, ln):
    dictionary = []
    for i in itertools.product(string, repeat=ln):
        dictionary.append(i)
    return dictionary


def sm(dc):
    some = []
    for element in dc:
        some.append(''.join(element))
    return some


def result(file, some):
    res = []
    for i in file:
        for j in some:
            if i == j:
                res.append(i)
    return res
