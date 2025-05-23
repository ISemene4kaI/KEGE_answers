"""
Какой минимальный объём памяти (в Кбайт) нужно зарезервировать, чтобы можно было сохранить любое растровое изображение размером 64 на 128
пикселей при условии, что в изображении могут использоваться 128 различных цветов? В ответе запишите только целое число, единицу измерения писать не
нужно.
"""

from math import log, ceil

a = 64*128*log(128, 2)
# Вначале считаем кол-во пикселей по его размерам. Далее умножаем на вес одного символа (он считается как логарифм по основанию 2).

b = ceil(a / 8 / 1024)
# Переводим в Кбайты с округлением вверх

print(b)

# ОТВЕТ: 7