import file


class Commands:
    def __init__(self):
        self.commands = []


    def add_commands(self, name, age, animal_type,command):
        self.commands.append({"name": name, "age": age, "animal_type": animal_type, "command": command})


    def get_info1(self):
        info = file.find_animals(path='note_animals.cvs')
        info1 = []
        name = info[0]
        info1.append(name)
        age = info[1]
        info1.append(age)
        animal_type = info[3]
        info1.append(animal_type)
        command = input("Введите новую команду: ")
        info1.append(command)

        return (info1)




