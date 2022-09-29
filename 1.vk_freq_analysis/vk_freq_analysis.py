"""
Программа состоит из трех основных частей:
1. Экспорт текстовых данных
2. Очистка текста
3. Частотный анализ

Исходные данные: letnyayashkola_vk.json
"""

import json
import re
import string
import pymorphy2
import nltk
from nltk.corpus import stopwords


# Часть 1. Экспорт текстовых данных
# Загрузка данных в формат python
with open('letnyayashkola_vk.json', 'r', encoding='utf-8') as file:
	data = json.load(file) # тип: список словарей

"""
Структура одного поста: structure_post.txt
текст поста, путь: data[i]/'text'
тексты комментов: data[i]/'textcomment'/'items'/'text'
для ответов: data[i]/'textcomment'/'items'/'thread'/'items'[j]:'text' 
"""

# Функция записывает текст в переменную text
def export_text(item, text):		# type(item) = dict
	text = text + item['text'] + '\n'
	if 'thread' in item.keys(): 	# для включения ответов на комментарии
		for reply in item['thread']['items']:
			return export_text(reply, text)
	return text


# Выгрузка постов и комментариев
posts, comments = '', ''
for post in data:
	posts = export_text(post, posts) 			# основной текст поста
	if post['textcomment']['items'] != []: 		# есть ли комментарии
		for comment in post['textcomment']['items']:
			comments = export_text(comment, comments)  # запись комментов



# Часть 2. Очистка текста
"""
Перед анализом текст необходимо "почистить". Нужно удалить из него: 
	- знаки препинания, цифры, служебные символы
	- стоп-слова (предлоги, союзы и т.д.)
	- обращения к сообществам и пользователям ("id72642677|Анастасия]")
	- ссылки
	- адреса электронных почт
	- хэштеги
"""

def clear_text(text):	# type(text) = str
	text = text.lower()	# перевод символов в нижний регистр

	# удаление фрагментов текста по шаблонам
	text = re.sub(r'(\[.*?\])', '', text) 			# обращения
	text = re.sub(r'https?://[^,\s]+', '', text) 	# ссылки
	text = re.sub(r'.*?@[^,\s]+', '', text)			# адреса почт
	text = re.sub(r'#[^,\s]+', '', text)			# хэштеги

	# удаление знаков пунктуации и цифр
	waste_chars = string.punctuation + string.digits + '«»…—'
	waste_chars = waste_chars.replace('-', '') # для слов с дефисом

	text = ''.join([ch for ch in text if ch not in waste_chars])
	text = text.replace('-', ' ') 	# разделение слов с дефисом на 2 слова
	text = text.replace(' — ', ' ') # для удаления тире

	# токенизация
	tokens = nltk.word_tokenize(text)

	# лемматизация
	morph = pymorphy2.MorphAnalyzer()
	lem_tokens = [morph.parse(w)[0].normal_form for w in tokens]

	# удаление стоп-слов (стоп-слова из стандартного набора nltk)
	stop_words = stopwords.words('russian')
	stop_words.extend(['это', 'очень', 'все', 'весь', 'который', 
		'наш', 'ваш', 'просто', 'вообще', 'свой', 'быть', 'ещё', 
		'всё', 'мочь'])

	main_tokens = [word for word in lem_tokens if not word in stop_words]
	text = nltk.Text(main_tokens) # преобразование к классу Text

	return text


posts = clear_text(posts)			# посты
comments = clear_text(comments)		# комментарии



# Часть 3. Частотный анализ текста и визуализация результатов
# type(text) = Text, obj - окончание названия графика
def freq_analysis(text, obj):
	fdist = nltk.FreqDist(text)		# словарь слово: частота
	fdist.plot(20, title=f'Самые частотные слова {obj}') # график
	print(fdist.most_common(20)) 	# вывод самых частотных слов


freq_analysis(posts, 'постов')				# посты
freq_analysis(comments, 'комментариев')		# комментарии