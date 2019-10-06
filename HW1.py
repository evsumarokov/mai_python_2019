#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ==================
# ДЗ №1: простые типы данных, изменяемые и неизменяемые типы, работа со строками, списки

# Задание: сделайте анализ выгрузки квартир с ЦИАН:

# 1) Измените структуру данных, используемую для хранения данных о квартире. Сейчас квартира = список. Сделайте вместо этого квартира = словарь следующего вида: flat_info = {"id":flat[0], "rooms":flat[1], "type":flat[2], "price":flat[11]}. В задании используйте поля: идентификатор квартиры на ЦИАН, количество комнат, тип (новостройка или вторичка), стоимость

# 2) Подсчитайте количество новостроек, расположенных у каждого из метро

import csv

# читаем информацию о квартирах в список flats_list
flats_list = list()
with open('output.csv', encoding="utf-8") as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)

# убираем заголовок
header = flats_list.pop(0)

# создаем словарь с информацией о квартирах
subway_dict = {}
for flat in flats_list:
	subway = flat[3].replace("м.", "")
	subway_dict.setdefault(subway, [])
	numb=None
	if flat[0].isdigit():
		numb=int(flat[0])
	flat_info = {"Тип":flat[2], "Номер": numb}

	subway_dict[subway].append(flat_info)

# TODO 2: подсчитайте и выведите на печать количество новостроек, расположенных рядом с каждым из метро. Используйте вариант прохода по словарю, который вам больше нравится
#for k,v in subway_dict:
    # используйте v для анализа значения
    # ваш код...
# либо
#for k in subway_dict:
    # используйте subway_dict[k] для анализа значения
    # ваш код...
for k, v in subway_dict.items():
    count = 0
    for i in v:
        if i["Тип"]=='новостройка':
            count=count+1
    print(f"У метро {k} {count} новостроек")


# In[ ]:





# In[ ]:




