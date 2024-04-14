import csv
from os.path import exists
from datetime import datetime


path = "note_animals.cvs"
path1 = "command_list_animals.cvs"

def path_file():
    if not exists(path):
        create_file_animals()
        return path
    return path


def path_file1():
    if not exists(path1):
        create_file_commands()
        return path1
    return path1


def create_file_animals():
    with open('note_animals.cvs', 'w', encoding='utf-8') as data:
        data.write("name,age,type\n")
        data.close()


def create_file_commands():
    with open('command_list_animals.cvs', 'w', encoding='utf-8') as data:
        data.write("name,age,type,commands\n")
        data.close()


def read_file(path):
    with open(path, 'r', encoding='utf-8') as data:
        registry = data.readlines()
        data.close()
    return registry


def read_file1(path1):
    with open(path1, 'r', encoding='utf-8') as data:
        commands = data.readlines()
        data.close()
    return commands

def write_file(info):
    with open(path, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]},{info[1]},{info[2]}\n')
    data.close()


def write_file1(info1):
    with open(path1, 'a', encoding='utf-8') as data:
        data.write(f'{info1[0]},{info1[1]},{info1[2]},{info1[3]}\n')
    data.close()


def find_animals(path):
    note_name = input("Введите имя для животного: ")
    with open(path, 'r', encoding='utf-8') as data:
        note_animals = data.readlines()
        animals_info = []
        for i, line in enumerate(note_animals):
            if note_name in line.strip():
                if i == 0:
                    print(f"fieldnames: ", line.strip())
                else:
                    print(f"Number №{len(animals_info) + 1}: ", line.strip())
                    animals_info.append(line.strip().split(','))
        if not animals_info:
            print("Животное не найдено в реестре.")
            return None
        flag = False
        while not flag:
            try:
                number = int(input("Выберите номер животного для обучения: "))
                if number < 0:
                    print('Неправильный номер')
                elif number > len(animals_info):
                    print('Животного с таким номером нет')
                else:
                    return animals_info[number - 1]
            except ValueError:
                print('Неверный номер')
