import Model
import View



def main_menu():
    while True:
        print('\nГлавное меню:')
        print('1. Добавить контакт')
        print('2. Удалить контакт')
        print('3. Изменить контакт')
        print('8. Сохранить файл')
        print('0. Выйти из программы')
        choice = int(input('Выберите пункт: '))
        match (choice):
            case 1:
                add_contact()
                print('\nКонтакт добавлен\n')
            case 2:
                remove_contact()
                print('\nКонтакт удален\n')
            case 3:
                change_contact()
            case 4:
                search_contact()
                print('\nКонтакт найден!\n')
            case 8:
                save_file()
                print('\nФайл сохранен!\n')
            case 0:
                break


def start():
    open_file()
    View.printPhoneBook()
    main_menu()



def open_file():
    with open(Model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        Model.phonebook = contacts_list

def save_file():
    with open(Model.path, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(Model.phonebook)))

def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    last_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {surname}; {last_name}; {phone};\n'
    Model.phonebook.append(contact)
    View.printPhoneBook()

def remove_contact():
    choice = int(input('Введите номер элемента для удаления: '))
    Model.phonebook.pop(choice)
    View.printPhoneBook()

def change_contact():

    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))

    contact = Model.phonebook.pop(choice).split(';')
    print(contact)
    contact[choice2] = input('Введите новое значение: ')
    print(contact)
    Model.phonebook.insert(choice, ';'.join(contact))
    View.printPhoneBook()

def search_contact():
    PhoneBook = {}
    choice = int(input('Введите элемент для поиска: '))

    contact = Model.phonebook.pop(choice).split(';')
    print(contact)  
    View.printPhoneBook()



#for _ in range(int(input())):
#    line = input().split()
#    if line[1] not in book:
#        book[line[1]] = [line[0]]
#    else:
#        phonebook[line[1]].append(line[0])
#for _ in range(int(input())):
#    print(*phonebook.get(input(), (['абонент не найден'])))