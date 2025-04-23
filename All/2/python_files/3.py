from itertools import permutations # Импорт библиотек/методов

def F(x,y,z): # Задаём функцию
    return ((not x) and y and z) or ((not x) and (not y) and z) or ((not x) and (not y) and (not z)) 
            # Пишем условное выражение, которое дано в самом начале

table = ((0,0,0),
         (1,0,0),
         (1,0,1))
    
if len(table) == len(set(table)): # Проверяем не совпадают ли строки таблицы
    for p in permutations("xyz"): # Перебираем возможные места переменных x,y,z,w
        if [F(**dict(zip(p, row))) for row in table] == [1,1,1]: # Сравниваем, подходит ли массив строк таблицы после обработки с необходимыми значениями функции
            print(p) # Выводим
            
#ОТВЕТ: zxy