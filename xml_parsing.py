#!/usr/bin/env python
"""
Анализирует xml файл на примере карты OSM по станице Шапсугской.
Сколько человек сделали отметки на карте. Сколько из них дали наименования своим точкам. 
Сколько сделали описания для точек.
"""

import requests
import xmltodict

#функция печати результатов выборки
def print_sample(kind, how_much):
# kind по какому признаку выборка
#   p количество точек
#   n количество наименований
#   d количество описаний
# how_much сколько позиций попадает в выборку
    for people in kind[:how_much]:
        if kind == p: print(people[0],people[1])
        if kind == n: print(people[0],people[2])
        if kind == d: print(people[0],people[3])

#из заданного каталога и имени файла в url собираем путь к файлу
path = 'shapsuga_map.osm'

#Считываем данные из файла в переменную xml
fin = open(path, 'r', encoding='utf8')
xml = fin.read()
fin.close()

users =[]
parsedxml = xmltodict.parse(xml)
for node in parsedxml['osm']['node']:
    if '@user' in node: users.append(node['@user']) #собираем всех users
users = list(set(users))            #выбираем из них уникальных
print('\nвсего героев: ', len(users)) 
user_data = []
for nic in users:
    user_data.append([nic])# собираем users  в список списков
for nic in user_data:    
    point = 0
    names = 0
    desc = 0
    for node in parsedxml['osm']['node']:
        if '@user' in node and node['@user'] == nic[0]:
            point += 1
        if 'tag' in node:
            tags = node['tag']
            if isinstance(tags, list):
                for tag in tags:
                    if tag['@k'] == 'name' and node['@user'] == nic[0] and tag['@v'] != '':
                        names += 1
                    if tag['@k'] == 'description' and node['@user'] == nic[0] and tag['@v'] != '':
                        desc += 1
    nic.append(point)
    nic.append(names)
    nic.append(desc)
p = sorted(user_data, key=lambda point:point[1], reverse=True)
n = sorted(user_data, key=lambda point:point[2], reverse=True)
d = sorted(user_data, key=lambda point:point[3], reverse=True)

print('\nНаиболее активные:')
print('По количеству отметок:')
print_sample(p,5)
print()
print('По количеству названий:')
print_sample(n,5)
print()
print('По количеству описаний:')
print_sample(d,2)
print()
