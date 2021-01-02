from WOW.big.hp import opn, sort, sm, result

file = opn('C:\\Programming\\Python\\my_programs\\WOW\\Букви\\aaajjj.txt')

string = input('Введіть букви слова: ')

ln = int(input('Вкажіть кількість букв у слові: '))
dc = sort(string, ln)

some = sm(dc)

result = result(file, some)
print(set(result))
