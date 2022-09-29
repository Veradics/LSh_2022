# Вторая часть кода
# Программа заменяет определенные формы слов на другие
# Слова (и их замены) хранятся в words_table.txt через ','

# Некоторые слова в списке уже указаны в нескольких формах, поэтому 
# поиск и замена не вошедших в список форм не проводились (вопрос - 
# как это можно сделать, если не вносить вручную?)

import re	# подключение модуля для регулярных выражений

# Считывание слов в словарь
# Ключ - заменяемое слово, значение - то, на что заменяется
rdict = {}
with open('words_table.txt', 'r', encoding='utf-8') as table:
	for line in table:
		pair = [i.rstrip() for i in line.split(',')]
		# strip() избавляет от служебных символов
		rdict[pair[0]] = pair[1]


# Функция replacer: принимает на вход 2 файла, считывает строки из f
# и записывает их с замененными словами в f_new
def replacer(f,f_new):
	for line in f:	
		str1 = line
		for key, value in rdict.items():
			str1 = re.sub(r'\b'+key+r'\b', value, str1)	# '\b' - граница слова
			str1 = re.sub(r'\b'+key.capitalize()+r'\b', value.capitalize(), str1)
			# позволяет заменять слова в начале предложения
		f_new.write(str1)


# Для статьи 1
with open('article_1.txt', 'r', encoding='utf-8') as f:
	with open('article_1_new.txt', 'w', encoding='utf-8') as f_new:
		rdict['язы́к'] = rdict['язык']	# для замены слова с ударением 
		replacer(f,f_new)

# Для статьи 2
with open('article_2.txt', 'r', encoding='utf-8') as f:
	with open('article_2_new.txt', 'w', encoding='utf-8') as f_new: 
		rdict['ёж'] = rdict['еж']
		replacer(f,f_new)

# Для статьи 3
with open('article_3.txt', 'r', encoding='utf-8') as f:
	with open('article_3_new.txt', 'w', encoding='utf-8') as f_new: 
		rdict['го́ты'] = rdict['готы']	# для замены слова с ударением 
		replacer(f,f_new)
