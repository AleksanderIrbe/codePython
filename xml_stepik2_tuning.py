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

#функция сохранения файла
def save_file(path):
    file = open(path, 'wb')
    file.write(r.content)
    file.close()    

#задаём адрес каталога, в котором будут находиться файлы
destination = 'xml_stepik'
print("по умолчанию каталог, в котором будут находиться файлы - " + destination)
print("если оставить его, введите '0', если изменить, введите название каталога: >> ")
dest = input()
if dest == '0':
    print('check: ' + os.path.abspath(destination))
else:
    destination = dest
#задаем ссылку на файл, который нужно скачать
url = 'https://stepik.org/media/attachments/lesson/245678/map1.osm'
print("по умолчанию url, из которого читается файл - " + url)
print("если оставить его, введите '0', если изменить, введите новый url: >> ")
ur = input()
if ur == '0':
    print('check: ' + url)
else:
    url = ur


#проверяем, создан ли уже каталог, если нет, то создаем
if not os.path.exists(destination):
    os.makedirs(destination)
    print('make new: ' + os.path.abspath(destination))


#из заданного каталога и имени файла в url собираем путь к файлу
path = os.path.abspath(destination) + '/' + os.path.basename(url)
print(is_accessible(path))

# проверяем наличие файла по указанному пути. Если файла нет, то запрашиваем его с url
if not is_accessible(path):
    r = requests.get(url) 
    #проверяем является ли файл архивом zip
    file_extention = os.path.splitext(url)
    if file_extention[1] == '.zip':
        while True:
            print('файл - архив "zip". Если разархивировать, нажмите "1", если скачать архивом, нажмите "2": >> ')
            code = input()
            if code == '1':
                with r, zipfile.ZipFile(io.BytesIO(r.content)) as archive:
                    archive.extractall(destination)
                break
            elif code == '2':
                save_file(path)
                break
            else:
                continue

    save_file(path)
else:
    print('file in catalog')

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