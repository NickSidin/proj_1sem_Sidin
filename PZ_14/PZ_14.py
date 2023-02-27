#Вариант 20. Из текстового файла writer.txt выбрать фамилии писателей и посчитать количество фамилий.
#Создать новый файл, в котором выполнить замену слова «роман» на «произведение».

import re

reg = re.compile(r'[А-ЯЁ][а-яё]+ [А-ЯЁ][,.][А-ЯЁ][,. ]|[А-ЯЁ][а-яё]+-[А-ЯЁ][а-яё]+ [А-ЯЁ][,.][А-ЯЁ][,. ]')
with open ('writer.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    surname = re.findall(reg, text)
    print(f'{surname}\n Количество фамилий писателей: {len(surname)}')

hello = re.compile(r'\b[Рр]оман\b')

with open('roman.txt', 'w', encoding='utf-8') as roman:
    roman.write(re.sub(hello, 'произведение', text))
    print(f"Количество замен слова Роман: {list(re.subn(hello, 'произведение', text))[-1]}")