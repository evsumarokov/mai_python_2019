#!/usr/bin/env python
# coding: utf-8




# ==================
# ДЗ №3: функции
# Дедлайн: 04 ноября 18:14
# Результат присылать на адрес nike64@gmail.com

# также прочитайте раздел "Функции" из книги "A byte of Python" (с.59)

# Задание: сделайте анализ возрастного состава группы студентов, используя функции.
# Помните, что а) у некоторых студентов отсутствуют данные по возрасту, б) возраст может быть задан диапазоном, например, 25-35. Поэтому не забывайте обрабатывать ошибки и исключения!

import csv

# помним, что в этот раз мы читаем не список списков, а список словарей!
# ключи в словаре для каждого студента называются по первой строчке из файла student_ages.csv: "Номер в списке", "Возраст"
ages_list = list()
with open('ages.csv', encoding="utf-8") as csvfile:
    ages_dictreader = csv.DictReader(csvfile, delimiter=',')
    ages_list = list(ages_dictreader)
#print (ages_list)
# подсказка: вот так мы можем получить данные из списка словарей
# именно так мы уже делали в коде лекции с квартирами
#for al in ages_list:
    #print(f'"Номер в списке": {al["Номер в списке"]}, "Возраст": {al["Возраст"]}')
    #print(al[])
# Задание 1: напишите функцию, которая разделяет выборку студентов на две части: меньше или равно указанного возраста и больше указанного возраста
# вернуться должна пара "Номер в списке, Возраст"
def filter_students_1(age, l):
	under_list = []
	upper_list = []
	unknownage_count = 0
	for i in l:
		a=str(i["Возраст"])
		if a == "" or "-" in a:
			unknownage_count +=1
		elif int(a) >= age:
			under_list.append(i)
			#print(1)
		elif int(a) < age:
			upper_list.append(i)
    # TODO 1: напишите ваш код проверки.
    # не забудьте исключить студентов, у которых возраст не указан, и подсчитать их количество

    # возвращаем результат из функции:
	return under_list, upper_list, unknownage_count
#print ("введите число")
#a=int(input())


# вызываем функцию:
#und_list, upp_list, unknwncount = filter_students_1(a, ages_list)
#print(f'"Выше или равно":\n {und_list}\n"Ниже":\n {upp_list}\n"не считает":\n {unknwncount}')

# Задание 2: улучшите функцию filter_students_1
# напишите функцию, которая принимает переменное количество параметров, каждый из которых может быть необязательным:
# Список и пример передачи параметров: age=30, warn=True, show_average=True
# 1) warn=True (False) - параметр, указывающий, что делать со студентами, которые не указали возраст:
# если возраст не указали значительно большее количество студентов, чем указали, выводите дополнительно предупреждение, что выборка неточная
# 2) show_average=True (False) нужно ли подсчитать и отобразить средний возраст студента.

# все параметры передавайте как **kwargs, т.е. пару "название параметра - значение параметра"
def get_average(l):
	count = 0
	average=0	
		
	for i in l:
		if "-" in i["Возраст"]:
			person_age = str(i["Возраст"]).split("-")				
			a = int(person_age[0])+int(person_age[1])
			average+=a/2
			count+=1
		elif i["Возраст"]!= "":
			average+=int(i["Возраст"])
			count+=1
		#print(i["Возраст"])
	a=average/count
	return a

def filter_students_2(l, **kwargs):
	'''	
	#Функция вывода групп студентов по возрасту
	## Подается словарь по типу номер студента , возраст 
	## Можно подать возраст для разбития по группам. Параметр age
	## Можно задать параметр процент заполнения возраста групп. Параметр percent_warn - int. ПО умолчанию 50%
	## warn - bool. 
	## Показать средний возраст выборки. Параметр show_average. bool
	'''	
	age=kwargs.get("age")
	percent=kwargs.get("percent_warn")
	if percent == None:
		percent=50
	if age == None:
		age=1	
	under_list = list()
	upper_list = list()
	unknownage_count = 0
	for i in l:
		a=str(i["Возраст"])
		if a == "" or "-" in a:
			unknownage_count +=1
		elif int(a) >= age:
			under_list.append(i)
			#print(1)
		elif int(a) < age:
			upper_list.append(i)
    # TODO 3: скопируйте сюда текст функции filter_students_1, которую вы написали ранее, и измените ее так, чтобы она работала с параметрами **kwargs
	warn_if_toomany = False
	if unknownage_count > len(l)*percent/100:
		warn_if_toomany = True
    # TODO 4: получите остальные два параметра по аналогии:
	if warn_if_toomany == kwargs.get("warn") and kwargs.get("warn")==True:
		print (f"Заполненные возрастные группы меньше {percent}. Заполните данные")
		return [],[],[]

    # TODO 5: сделайте проверку. Если значение параметра warn, show_average = True, выполните соответствующую обработку. Например:
    #if warn_if_toomany == True:
    # напишите здесь код проверки и вывод предупреждающего сообщения пользователю
	show_average = kwargs.get("show_average")
	if show_average == True:
		print(get_average(l))
    # напишите здесь код подсчета и вывода среднего значения возраста студентов

    # возвращаем результат из функции:
	return under_list, upper_list, unknownage_count


# вызываем функцию filter_students_2

und_list, upp_list, unknwncount = filter_students_2(ages_list, age=30, percent_warn=70, warn=True, show_average=True)
print(f'"Выше или равно":\n {und_list}\n"Ниже":\n {upp_list}\n"не считает":\n {unknwncount}', filter_students_2.__doc__)
