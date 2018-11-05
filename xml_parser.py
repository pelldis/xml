#-*- coding: utf-8 -*-
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET
import sys
import os

#функция парсинга
def getTitles(xml):
	"""
	Выводим все заголовки из xml.
	"""
	doc = minidom.parse(xml)
	node = doc.documentElement
	# парсим данные по тегу, данные впоследсвие будем доставать из books 
	books = doc.getElementsByTagName("Row")
	
	titles = []
	# включаем счетчик для выбора данных с нужной строки
	count1=0
	for book in books:
		#print(book)
		for i in range(3,5):
		#Указываем с какой строки брать данные, будут браться с count1+1 например если 6, то с 7
			if count1 >= 6: 
		
				#print book.getElementsByTagName("Data")[2]
				titleObj = book.getElementsByTagName("Data")[i]
				titles.append(titleObj)
		count1+= 1
	print
	
	
	'''for title in titles:
		nodes = title.childNodes
		for node in nodes:
			#if node.nodeType == node.TEXT_NODE:
			print(node.data) '''

#count = 0
def editXML(directory, filename):
	tree = ET.parse(filename)
	root = tree.getroot()
	print ("tag=%s, attrib=%s" % (root.tag, root.attrib))
	for child in root:
		print child.tag, child.attrib
	print "-" * 40
	print 'Iterating using a tree iterator'
	print "-" * 40
	iter_ = tree.getiterator()
	n=0
	for elem in iter_:
		if "Row" in elem.tag:
			if n > 1:
				print n
			n += 1
			z=0
		elif "Data" in elem.tag:
			if z == 3:
				elem.text = "50000"
			z += 1
			print elem.text,
	iter_ = tree.getiterator()
	for elem in iter_:
		if "Data" in elem.tag:
			print elem.text
	#print tree
	#print "\n"
	#appointments = root.getchildren()
	'''for appointment in appointments:
		appt_children = appointment.getchildren()
		for appt_child in appt_children:
			print("%s=%s" % (appt_child.tag, appt_child.text))'''
	# задаем начальный столбец - #2
	#z=2
	# делаем количество циклов = количество значений со второго столбца до конца строки
	# деленое на 2, т.к. uplink, downlink - это одна итерация
	'''for n in range((len(root[3][0][7][2::]))/2):
		# указываем интервал строк, по которым будет идти итерация (x, y+1) 
		for i in range(7,17):
			# указываем номера столбцов итерации x,x+1
			for j in (z,z+1):
				print root[3][0][i][j][0].text,
			print
		z+=2'''
	
	#tree = ET.ElementTree(root)
	#print root[0]
	#with open("vygruzka1.xml", "w") as f:
	#	print row
# Указываем директорию, из которой будем открывать файлы для парсинга	
#directory = "/home/antosh/Documents"
files = os.listdir(directory)
# Парсим все файлы заканчивающиеся на .xml с помощью ранее созданной функции
'''for i in sorted(files):
	if i.endswith(".xml"):
		#print i
		getTitles(i)'''
		
editXML("vygruzka.xml")


		
		
	
