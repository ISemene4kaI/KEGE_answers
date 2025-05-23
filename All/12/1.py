"""
Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 70 идущих подряд цифр 8? В ответе запишите
полученную строку.
НАЧАЛО
ПОКА нашлось (2222) ИЛИ нашлось (8888)
    ЕСЛИ нашлось (2222)
        ТО заменить (2222, 88)
        ИНАЧЕ заменить (8888, 22)
    КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
"""

a = '8' * 70 # "70 идущих подряд цифр 8"

# Переводим псевдокод в код Python
while "2222" in a or "8888" in a:
    if '2222' in a:
        a = a.replace('2222', '88', 1)
    else:
        a = a.replace('8888', '22', 1)
        
print(a) # Вывод

# ОТВЕТ: 22