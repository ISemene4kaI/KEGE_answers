"""
Для хранения в информационной системе документы сканируются с разрешением 600 ppi и цветовой системой, содержащей 2**24 = 1 6 777 216 цветов. Методы
сжатия изображений не используются. Средний размер отсканированного документа составляет 12 Мбайт. В целях экономии было решено перейти на
разрешение 300 ppi и цветовую систему, содержащую 256 цветов. сколько Мбайт будет составлять средний размер документа, отсканированного с
изменёнными параметрами?
"""

from math import log

a = 600**2 / 300**2 
# Находим насколько изменилось кол-во пикселей на один инч (ppi - pixel per inch)

b = 24 / log(256, 2)
# Считаем изменение веса символа

c = 12 / a / b
# Делим начальный размер файла, на изменение его параметров и находим нужный размер

print(c)

# ОТВЕТ: 1