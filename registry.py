class Registry:
    def __init__(self):
        self.registry = []

    def add_animal(self, name, age, animal_type):
        self.registry.append({"name": name, "age": age, "type": animal_type})

    def print_available_types(self):
        available_types = ['собака', 'кошка', 'хомяк']
        print("Доступные типы животных:")
        for animal_type in available_types:
            print("-", animal_type)

    def get_info(self):
        info = []
        name = input("Введите имя животного: ")
        info.append(name)
        age = input("Введите возраст животного: ")
        info.append(age)
        self.print_available_types()
        while True:
            animal_type = input("Выберите тип животного (собака, кошка, хомяк): ")
            if animal_type.lower() in ['собака', 'кошка', 'хомяк']:
                info.append(animal_type.lower())
                break
            else:
                print("Такого типа животного нет. Пожалуйста, выберите из доступных.")

        return (info)

