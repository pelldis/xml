#-*- coding: utf-8 -*-
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET
import sys
import os


def get_data_xml(filename):
	tree = ET.parse(filename)
	root = tree.getroot()
	iter_ = tree.getiterator()
	data = []
	n = 0 # счетчик строк
	for elem in iter_: 
		#print n, elem.tag
		# проходим по файлам откуда забирать значения
		if "Row" in elem.tag:
			z = 0 # счетчик столбцов
			n += 1

		elif "Data" in elem.tag and n > 6:
			if z > 1 and z < 4: # Берем данные из 3 и 4 столбца
				print elem.text,
				data.append(int(elem.text)) # Добавляем значение в список
				z += 1
			else:
				z += 1
	#print data   #, data.pop(0)
	return data
#get_data_xml("one1.xml")

def editXML(directory, filename):
	files = os.listdir(directory)
	num = 2 # счетчик для перехода через 2 столбца каждый новый файл
	for file_ in sorted(files): # парсим каждый файл в сортированном виде
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
				#print n, elem.tag
				# проходим по файлам откуда забирать значения
				if "Row" in elem.tag:
					z = 0 # счетчик столбцов
					n += 1

				elif "Data" in elem.tag and n > 6:
					if z in range(num, num+2): # Берем данные из 2 и 3 столбца
						print elem.text, int(a[c])
						elem.text = str(a[c])
						c += 1
						z += 1
					else:
						z += 1
			num += 2
			#vyvod = tree.getroot()
			#iter_ = tree.getiterator()
			for elem in iter_:
				if "Data" in elem.tag:
					print elem.text
			tree.write("vygruzka.xml")
			
			
directory = "/home/antosh/Documents"
editXML(directory, "vygruzka.xml")
