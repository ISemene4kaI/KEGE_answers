"""
Сколько нулей будет в преобразованной строке после выполнения следующего алгоритма для строки, состоящей из 1 и идущих за ней 33 нулей?

НАЧАЛО
ПОКА нашлось(1) или нашлось(100)
    ЕСЛИ нашлось(100)
        ТО заменить(100, 0001)
        ИНАЧЕ заменить(1, 00)
    КОНЕЦ ЕСЛИ
КОНЕЦ пока
КОНЕЦ

"""

a = '1' + '0'*33 # "Строки, состоящей из 1 и идущих за ней 33 нулей"

# Переводим псевдокод в код Python
while '1' in a or '100' in a:
    if '100' in a:
        a = a.replace("100", "0001", 1)
    else:
        a = a.replace("1", '00', 1)
        
print(a.count('0')) # Вывод кол-ва нулей

# ОТВЕТ: 51