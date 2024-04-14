import commands
import file
import registry
import counter

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
    with counter.Counter() as counter1:
        info = info_0.get_info()
        file.write_file(info)
        counter1.add()
    info = info_0.get_info()
    file.write_file(info)


def add_commands():
    info_1 = commands.Commands()
    info1 = info_1.get_info1()
    file.write_file1(info1)


def find_note():
    path = file.path_file()
    contact = file.find_animals(path)
    print(contact)


def print_available_types():
    print("Доступные типы животных:")
    print("- собака")
    print("- кошка")
    print("- хомяк")
