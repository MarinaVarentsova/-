import commands
import file
import registry


def show_animals():
    path = file.path_file()
    data = file.read_file(path)
    print(data)

def show_commands():
    path1 = file.path_file1()
    data1 = file.read_file1(path1)
    print(data1)

def add_animals():
    file.path_file()
    info_0 = registry.Registry()
    info = info_0.get_info()
    file.write_file(info)

def add_commands():
    # path = file.path_file()
    # info = file.find_animals(path)
    # info1 = []
    # name = info[0]
    # info1.append(name)
    # age = info[1]
    # info1.append(age)
    # animal_type = info[2]
    # info1.append(animal_type)
    # command = input("Введите новую команду: ")
    # info1.append(command)
    info_1 = commands.Commands()
    info1 = info_1.get_info1()
    file.write_file1(info1)


def find_note():
    path = file.path_file()
    contact = file.find_animals(path)
    print(contact)


def print_available_types(self):
    print("Доступные типы животных:")
    print("- собака")
    print("- кошка")
    print("- хомяк")

# def save_to_file(self):
#     with open("animal_registry.txt", "w") as file:
#         for animal in self.registry:
#             file.write(f"Имя: {animal['name']}, Возраст: {animal['age']}, Тип: {animal['type']}\n")



# def delete_note():
#     path = file.path_file()
#     contact = file.find_for_change_file(path)
#     print(file.delete_file(path, contact))