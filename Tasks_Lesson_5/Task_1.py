""" Напишите программу, удаляющую из текста все слова, содержащие ""абв"". """

def SortWords(textLocal):

    words = textLocal.split()

    filtered_words = []

    for word in words:
        if 'а' in word or 'б' in word or 'в' in word:
            continue  #Если слово содержит нужные буквы, пропускаем его
        else:
            filtered_words.append(word)
    result = ' '.join(filtered_words)  # Объединяем список отфильтрованных слов обратно в текст
    return result

text = input("Введите текст: ")
print(SortWords(text))