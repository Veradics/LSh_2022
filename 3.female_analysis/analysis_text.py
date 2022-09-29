"""
Программа убирает стоп-слова и визуализирует 20 самых частотных слов
Включено: очистка текста, токенизация, частотный анализ

Лемматизация не проводилась, т.к. было замечено, что в списке предлагаемых 
стоп-слов содержатся разные формы одних и тех же слов

Текст: female.txt (с удаленным вручную английским текстом в начале и конце)
Стоп-слова: stopwords.txt
"""

import string
import nltk


# Часть 1. Загрузка данных
# Чтение текста из файла
with open('female.txt', 'r', encoding='utf-8') as f:
	text = f.read()

# Загрузка стоп-слов из файла
stopwords = []	
with open('stopwords.txt', 'r', encoding='utf-8') as stopfile:
	for line in stopfile:
		stopwords.append(line.strip())



# Часть 2. Предварительная обработка текста
text = text.lower()	# перевод символов в нижний регистр

# удаление знаков препинания, спец.символов и цифр
waste_chars = string.punctuation + string.digits + '«»”…'
waste_chars = waste_chars.replace('-', '')	# т.к. есть слова с дефисом

text = ''.join([ch for ch in text if ch not in waste_chars])
text = text.replace('-', ' ') # разделение слов с дефисом на два слова
text = text.replace('—', ' ') # в тексте рядом с '—' нет пробелов
# print(text)

# токенизация (разбиение на отдельные слова)
tokens = nltk.word_tokenize(text) # тип: список

# удаление стоп-слов
main_tokens = [word for word in tokens if not word in stopwords]

# преобразование к классу Text
text = nltk.Text(main_tokens)



# Часть 3. Частотный анализ
# Подсчет статистики распределения частот слов в тексте
fdist = nltk.FreqDist(text)		# словарь слово: частота
print(fdist.most_common(20))	# вывод 20 самых частотных слов (кортеж)

# Визуализация распределения частот
fdist.plot(20, title='20 самых частотных слов текста')	# график