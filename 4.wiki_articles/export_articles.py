# pip install wikipedia

# Первая часть кода
# Программа извлекает статьи из Википедии и записывает их в файлы .txt

import wikipedia			# подключение доп.модуля
wikipedia.set_lang('ru') 	# язык: русский
 
with open('article_1.txt', 'w', encoding='utf-8') as article_1:
	article_1.write(wikipedia.page('Язык (анатомия)').content)

with open('article_2.txt', 'w', encoding='utf-8') as article_2:
	article_2.write(wikipedia.page('Обыкновенный ёж').content)

with open('article_3.txt', 'w', encoding='utf-8') as article_3:
	article_3.write(wikipedia.page('Готы (субкультура)').content)
