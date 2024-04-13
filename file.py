import csv
from os.path import exists
from datetime import datetime


path = "note_animals.cvs"
path1 = "command_list_animals"

def path_file():
    if not exists(path):
        create_file_animals()
        return path
    return path


def path_file1():
    if not exists(path1):
        create_file_animals()
        return path1
    return path1


def create_file_animals():
    with open('note_animals.cvs', 'w', encoding='utf-8') as data:
        data.write("name,age,type\n")
        data.close()


def create_file_commands():
    with open('command_list_animals', 'w', encoding='utf-8') as data:
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


# def find_animals(path):
#     note_name = input("введите имя для животного: ")
#     with open(path, 'r', encoding='utf-8') as data:
#         note_animals = data.readlines()
#         for i, line in enumerate(note_animals):
#             if note_name in line.strip():
#                 if i == 0:
#                     print(f"fieldnames: ", line.strip())
#                 else:
#                     print(f"Number №{i}: ", line.strip())
#         flag = False
#         while not flag:
#             try:
#                 number = int(input("выберите номер животного для обучения: "))
#                 if number < 0:
#                     print('wrong note')
#                     flag = False
#                 if number == 0:
#                     number = 0
#                     flag = True
#                 if number > 0:
#                     number = number - 1
#                     flag = True
#                 else:
#                     flag = True
#             except ValueError:
#                 print('not valid note')
#         return number
def find_animals(path):
    note_name = input("Введите имя для животного: ")
    with open(path, 'r', encoding='utf-8') as data:
        note_animals = data.readlines()
        animals_info = []  # Создаем список для хранения информации о животных
        for i, line in enumerate(note_animals):
            if note_name in line.strip():
                if i == 0:
                    print(f"fieldnames: ", line.strip())
                else:
                    print(f"Number №{i}: ", line.strip())
                    # Разделяем строку на отдельные элементы и добавляем в список информации о животном
                    animals_info.append(line.strip().split(','))
        flag = False
        while not flag:
            try:
                number = int(input("Выберите номер животного для обучения: "))
                if number < 0:
                    print('Неправильный номер')
                elif number > len(animals_info):
                    print('Животного с таким номером нет')
                else:
                    return animals_info[number - 1]  # Возвращаем информацию о животном по его индексу
            except ValueError:
                print('Неверный номер')



# def delete_file(path, number):
#     with open(path, "r") as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         note_book = []
#         for row in csv_reader:
#             print(row)
#             note_book.append(row)
#     print('\n')
#     to_update = note_book[number].values()
#     number_1 = number + 1
#     print(f"Number №{number_1} будет удален, текущие данные: ", to_update)
#     valid = input("подтвердите удаление Y/N: ")
#     if valid == 'Y':
#         with open(path, 'w', newline='') as csv_file:
#             fieldnames = note_book[0].keys()
#             writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#             writer.writeheader()
#             note_book.pop(number)
#             for row in note_book:
#                 writer.writerow(row)
#                 print(row)
#     else:
#         print('Номер заметки для удаления не выбран')




