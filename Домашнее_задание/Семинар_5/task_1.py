# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('Введите строку: ')
word_search = input('Введите буквосочетание для удаления: ')

text_list = text.split(' ')
new_text_list = []
for i in text_list:
    if i.find(word_search) == -1:
        new_text_list.append(i)

new_text = ' '.join(new_text_list)
print(new_text)