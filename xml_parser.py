#-*- coding: utf-8 -*-
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET
import sys
import os

# функция для сбора значений из двух рядом стоящих ячеек в список []
def get_data_xml(filename):
	tree = ET.parse(filename)
	root = tree.getroot()
	iter_ = tree.getiterator()
	data = []
	n = 0 # счетчик строк
	for elem in iter_: 
		# проходим по файлам откуда забирать значения
		if "Row" in elem.tag:
			z = 0 # счетчик столбцов
			n += 1

		elif "Data" in elem.tag and n > 6:
			if z > 1 and z < 4: # Берем данные из 3 и 4 столбца
				# Добавляем значение в список
				data.append(int(elem.text)) 
				z += 1						
			else:
				z += 1
	#print data   #, data.pop(0)
	return data
# функция для обхода файлов xml в указанной директории с вложенной 
# функцией сбора значений, изменение значений файла filename
# в двух столбцах для каждого файла и запись в файл filename
def editXML(directory, filename):
	files = os.listdir(directory)
	num = 2 # счетчик для перехода через 2 столбца каждый новый файл
	# парсим каждый файл в сортированном виде
	for file_ in sorted(files): 
		# если файл - xml и не основной файл
		if file_.endswith(".xml") and "vyg" not in file_:
			print
			print "* * * Парсим файл", file_, " * * *\n" 
			a = list(get_data_xml(file_))
			print a
			tree = ET.parse(filename)
			root = tree.getroot()
			iter_ = tree.getiterator()
			
			n = 0 # счетчик строк
			c = 0 # счетчик для элемента в листе дочернего файла
			for elem in iter_: 
				# итерация файла filename
				# Row - тэг строки в дереве
				if "Row" in elem.tag:
					z = 0 # счетчик столбцов
					n += 1 #
				# проверяем значения с 7 строки для редактирования
				elif "Data" in elem.tag and n > 6:
					# Берем данные из 2 и 3 столбца
					if z in range(num, num+2): 
						#print elem.text, int(a[c])
						# Обязательно преобразуем число в строку
						elem.text = str(a[c])
						c += 1
						z += 1
					else:
						z += 1
			num += 2
			# пишем в файл после обхода каждого файла
			tree.write("vygruzka.xml", encoding="UTF-8")
	# выводим в терминал то, что записали в файл
	for elem in iter_:
		if "Row" in elem.tag:
			print
		elif "Data" in elem.tag:
			print "{:<14}".format(elem.text),
					
directory = "/home/antosh/Documents"
# вызов функции
editXML(directory, "vygruzka.xml")
