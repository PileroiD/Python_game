import itertools

answer = input('Вкажіть першу букву слова: ')
with open(f'C:\\Programming\\Python\\my_programs\\WOW\\Букви\\{answer}.txt', encoding='utf8') as file:
    new_file = file.read()
new_file = new_file.split()
# print(new_file)


string = input('Введіть букви слова: ')
# print(string)
dictionary = []

ln = int(input('Вкажіть кількість букв у слові: '))
for i in itertools.product(string, repeat=ln):
    dictionary.append(i)
# print(dictionary)

some = []
for element in dictionary:
    some.append(''.join(element))
# print(some)

result = []
for element1 in new_file:
    for element2 in some:
        if element1 == element2:
            result.append(element1)
print(set(result))
