import json

# Загрузка данных в формат python
with open('letnyayashkola_vk.json', 'r', encoding='utf-8') as file:
	data = json.load(file)

# print(type(data)) # тип: список словарей
# print(data[0]) 	# пример одного компонента списка (data_example.txt)


# Определение иерархии структуры записи поста
# "узлом" в cхеме может быть list или dict

# Программа принимает на вход словарь и файл для записи
# параметр tab - отступ от начала строки

def str_dict(dictionary, f, tab):
	for key, value in dictionary.items():
		f.write(tab + '- ' + str(key) + '\n')

#		if type(value) in [str, int, bool]:		# если необходима вся инфа
#			f.write('\t' + tab + '- ' + str(value) + '\n')

		if type(value) == list:	 				# если список массивов 
			for i in value:						# если вся инфа: elif
				if type(i) == dict:
					str_dict(i, f, tab +'\t')	# отступ на новый уровень

		elif type(value) == dict:				# если словарь
			str_dict(value, f, tab +'\t')		# отступ на новый уровень

	tab = tab[:-2]
	f.write(' \n')


# Анализ структуры второго поста
with open('structure_post.txt', 'w', encoding='utf-8') as f:
	str_dict(data[1], f, '')










