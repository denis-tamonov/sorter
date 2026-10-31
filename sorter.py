#!/usr/bin/env python3

import os

def sorter(edit_with, copy_with):

    if copy_with == '':
        copy_with = os.path.expanduser('~/Documents/') #Функция os.path.expanduser(path) из стандартной библиотеки Python используется для замены символа тильды (~ или ~user) в пути на полный путь к домашней директории пользователя.

    if not (edit_with.startswith('/home/') or edit_with.startswith('~')):
        edit_with = os.path.join(os.path.expanduser("~/Documents/"), edit_with) #Функция os.path.join(path, *paths) предназначена для корректного объединения одного или нескольких компонентов пути в одну строку, учитывая особенности операционной системы.
    else:
        edit_with = os.path.expanduser(edit_with)

    if edit_with.endswith('.txt'):

        open_list_with_n = open(f'{edit_with}').readlines()
        open_list_without_n = [line.rstrip('\n') for line in open_list_with_n]
    else:
        open_list_with_n = open(f'{edit_with}.txt').readlines()
        open_list_without_n = [line.rstrip('\n') for line in open_list_with_n]

    sorter_list = sorted(open_list_without_n)
    c = input("Введите название файла, котрое будет после сортировки (Enter для default):")
    if c =="" or c==" " or c == "\n":
        c = "After_sort_text"
    new_file = open(f'{copy_with}{c}.txt', "+w")

    for u in range(len(sorter_list)):
         new_file.write(sorter_list[u] + '\n')
    print(f"Готово! Файл {c} сохранен в: {copy_with}")
    return new_file



a = input("Введите путь к файлу: ")
b = input("Введите путь для сохранения (Enter для default): ")
sorter(a, b)
