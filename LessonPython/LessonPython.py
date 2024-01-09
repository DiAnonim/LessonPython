#Задание №1.
#Реализуйте программу, чтобы найти дату первого понедельника данной недели. 
#Date: 2015, 50
#Output: пн 14 декабря 00:00:00 2015
#from datetime import datetime, timedelta

#def find_first_monday(year, week):
#    firstDay = datetime(year, 1, 1)

#    daysDifference = (7 - firstDay.weekday()) % 7

#    daysDifferenceWeek = (week - 1) * 7

#    monday = firstDay + timedelta(days=daysDifference + daysDifferenceWeek)

#    return monday

#resDate = find_first_monday(2015, 50)
#print(resDate.strftime("%a %d %B %H:%M:%S %Y"))

#Задание №2
#Реализуйте программу, для преобразования двух 
#разностей дат в дни, часы, минуты и секунды

#from datetime import datetime, timedelta

#def differenceDates(diff):
#    total_seconds = diff.total_seconds()

#    d = int(total_seconds // (24 * 3600))
#    h = int((total_seconds % (24 * 3600)) // 3600)
#    m = int((total_seconds % 3600) // 60)
#    s = int(total_seconds % 60)

#    return d, h, m, s

#d1 = datetime(2023, 1, 1, 12, 0, 0)
#d2 = datetime(2023, 1, 5, 18, 30, 15)

#time_difference = d2 - d1

#days, hours, minutes, seconds = differenceDates(time_difference)

#print(f"The difference between the dates: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")

#Задание №3
#Дан текстовый файл. Необходимо создать новый файл 
#убрав из него все неприемлемые слова. Список 
#неприемлемых слов находится в другом файле.

#def filter_words(inpFile, filtFile, outFile):
#    with open(inpFile, 'r', encoding='utf-8') as input_file:
#        text_content = input_file.read()

#    with open(filtFile, 'r', encoding='utf-8') as filter_file:
#        unacceptable_words = set(filter_file.read().split())

#    filtered_text = ' '.join(word for word in text_content.split() if word.lower() not in unacceptable_words)

#    with open(outFile, 'w', encoding='utf-8') as output_file:
#        output_file.write(filtered_text)

#filter_words('input.txt', 'unacceptable_words.txt', 'output.txt')


#Задание №5
#В текущей папке лежат две другие папки: video и sub. 
#Создайте новую папку watch_me и переложите туда 
#содержимое указанных папок (сами папки класть не надо).
#import os
#import shutil

#def contents(sourceDir, destinationDir):
#    if not os.path.exists(destinationDir):
#        os.makedirs(destinationDir)

#    for item in os.listdir(sourceDir):
#        source_item = os.path.join(sourceDir, item)
#        destination_item = os.path.join(destinationDir, item)

#        if os.path.isdir(source_item):
#            shutil.move(source_item, destination_item)

#watch_me_folder = 'watch_me'

#contents('video', watch_me_folder)
#contents('sub', watch_me_folder)

#print(f'Content video and sub successfully moved to {watch_me_folder}.')



#Задание №6
#В текущей папке лежат файлы типа 
#Nina_Stoletova.txt, Misha_Perelman.txt и т.п. 
#Переименуйте их переставив имя и фамилию местами.

#import os

#def rename(direc):
#    for filename in os.listdir(direc):
#        name, extension = os.path.splitext(filename)

#        parts = name.split('_')
#        if len(parts) == 2:
#            first_name, last_name = parts
#            new_filename = f"{last_name}_{first_name}{extension}"

#            old_path = os.path.join(direc, filename)
#            new_path = os.path.join(direc, new_filename)

#            os.rename(old_path, new_path)

#            print(f'file {filename} ren to {new_filename}.')

#rename('test')





