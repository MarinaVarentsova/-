import registry
import function


def list_program():
    print('\n Выберите команду по работе с заметками: '
          '\n 1 - посмотреть реестр животых'
          '\n 2 - добавление нового животного в реестр'
          '\n 3 - добавление новой команды животному'
          '\n 4 - посмотреть список команд животного'
          '\n 5 - выход')


def run():
    while True:
        list_program()
        command = input('Введите команду: ')
        if command == '1':
            function.show_animals()
        elif command == '2':
            function.add_animals()
        elif command == '3':
            function.add_commands()
        elif command == '4':
            function.show_commands()
        elif command == '5':
            break
        else:
            print('Ошибка ввода команды')
