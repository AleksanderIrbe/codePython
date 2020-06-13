#!/usr/bin/env python
import requests
import xmltodict
import os

# функция проверки наличия файла путем попытки открыть его    
def is_accessible(path, mode='r'):
    """
    Проверка, является ли файл или папка из `path`
    доступным для работы в предоставленным `mode` формате.
    """
    try:
        f = open(path, mode)
        f.close()
    except IOError:
        return False
    return True


#задаём адрес каталога, в котором будут находиться файлы
destination = 'xml_stepik'
#задаем ссылку на файл, который нужно скачать
url = 'https://stepik.org/media/attachments/lesson/245678/map1.osm'


#проверяем, создан ли уже каталог, если нет, то создаем
if not os.path.exists(destination):
    os.makedirs(destination)
    print('make new: ' + os.path.abspath(destination))
else:
    print('check: ' + os.path.abspath(destination))

#из заданного каталога и имени файла в url собираем путь к файлу
path = os.path.abspath(destination) + '/' + os.path.basename(url)

# #проверяем, скачали ли уже архив, если нет, то скачиваем
# if not os.listdir(destination):
#     #скачиваем и распаковываем архив
#     r = requests.get(url)
#     #проверяем является ли файл архивом zip, если да, то разархивируем
#     file_extention = os.path.splitext(url)
#     if file_extention[1] == '.zip':
#         with r, zipfile.ZipFile(io.BytesIO(r.content)) as archive:
#             archive.extractall(destination)
#     #если нет, то сохраняем в каталог
#     else:
#         file = open('./' + destination + '/' + os.path.basename(url), 'wb')
#         file.write(r.content)
#         file.close()


# fin = open('./' + destination + '/' + os.path.basename(url), 'r', encoding='utf8')
# xml = fin.read()
# fin.close()

# yes = 0
# no = 0
# parsedxml = xmltodict.parse(xml)
# for node in parsedxml['osm']['node']:
#     if 'tag' in node:
#         yes += 1
#     if 'tag' not in node:
#         no += 1
# print(yes,no)