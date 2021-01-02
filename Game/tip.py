from pprint import pprint

answer = int(input('Сколько букв в вашем слове: '))
answer1 = input('Скажите первую букву вашего слова: ')
answer2 = input('Скажите второю букву вашего слова: ')
answer3 = input('Скажите третью букву вашего слова: ')
answer4 = input('Скажите четвёртую букву вашего слова: ')

with open('C:\\Python\\Просто для практики\\WordsStockRus.txt', encoding='utf8') as file:
    new_file = file.read()
new_file = new_file.split()

words_list = []
for element in new_file:
    if len(element) == answer:
        words_list.append(element)
# print(words_list)

if answer1:
    res1 = [letteer for letteer in words_list if letteer[0] == answer1]
    # pprint(res1)

if answer2:
    res2 = [lettee for lettee in words_list if lettee[1] == answer2]
    # pprint(res2)

if answer3:
    res3 = [lett for lett in words_list if lett[2] == answer3]
    # pprint(res3)

if answer4:
    res4 = [lett for lett in words_list if lett[3] == answer4]
    # pprint(res4)

final = []
if answer1 and answer2:
    for q in res1:
        if q in res2:
            print(q)
elif answer1 and answer3:
    for w in res1:
        if w in res3:
            print(w)
elif answer1 and answer4:
    for e in res1:
        if e in res4:
            print(e)
elif answer2 and answer3:
    for r in res2:
        if r in res3:
            print(r)
elif answer2 and answer4:
    for t in res2:
        if t in res4:
            print(t)
elif answer3 and answer4:
    for y in res3:
        if y in res4:
            print(y)

