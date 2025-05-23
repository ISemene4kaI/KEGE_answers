"""
Дана программа для Редактора:

НАЧАЛО
ПОКА нашлось (>1) ИЛИ нашлось (>2) ИЛИ нашлось (>3)
    ЕСЛИ нашлось (>1)
        ТО заменить (>1, 22>)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (>2)
        ТО заменить (>2, 2>)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (>3)
        ТО заменить (>3, 1>)
КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ

На вход приведённой ниже программе поступает строка, начинающаяся с символа «>», а затем содержащая 11 цифр 1, 12 цифр 2 и 30 цифр З, расположенных
в произвольном порядке.
Определите сумму числовых значений цифр строки, получившейся в результате выполнения программы. Так, например, если результат работы программы
представлял бы собой строку, состоящую из 50 цифр 4, то верным ответом было бы число 200.
"""

a = ">" + '1' * 11 + '2' * 12 + '3' * 30 # Строка, начинающаяся с символа «>», а затем содержащая 11 цифр 1, 12 цифр 2 и 30 цифр З

# Переводим псевдокод в код Python
while '>1' in a or '>2' in a or '>3' in a:
    if ">1" in a:
        a = a.replace(">1", "22>", 1)
    if ">2" in a:
        a = a.replace(">2", "2>", 1)
    if ">3" in a:
        a = a.replace(">3", "1>", 1)
        
print(sum(int(el) for el in a.replace(">", ""))) 
# Преобразуем каждую цифру в число (обязательно убрать ">" из строки, иначе будет ошибка) и считаем сумму всех чисел, после, выводим ответ

# ОТВЕТ: 98