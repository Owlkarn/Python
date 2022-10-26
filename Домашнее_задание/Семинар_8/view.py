import controller

def show_menu():
    print('0. Показать все контакты')
    print('1. Открыть файл с контактами')
    print('2. Записать файл с контактами')
    print('3. Добавить контакт')
    print('4. Изменить контакт')
    print('5. Удалить контакт')
    print('6. Поиск по контактам')
    choise = int(input('Выберите пункт меню: '))
    return choise

def show_phone_book(phone_book):
    if len(phone_book) < 1:
        print('Телефонная книга пуста')
    else:
        for id, contact in enumerate(phone_book):
            print(id, *contact)
            
def input_path():
    path = input('Введите имя файла: ')
    return path
        
def input_contact():
    name_contact = input('Введите фамилию и имя контакта: ')
    phone_contact = input('Введите телефон контакта: ')
    comment_contact = input('Введите комментарий: ')
    return (name_contact, phone_contact, comment_contact)

def change_contact():
    id = int(input('Введите номер контакта: '))
    choise = input('0 - имя, 1 - телефон, 2 - комментарий, 3 - отмена: ')
    if choise != '3':
        value = input('Введите новое значение: ')
        return(id, choise, value)
    else:
        controller.start()

def save_how():
    path = input('Сохранить файл как: ')
    return path

def get_index_del_element():
    del_el = int(input('Введите индекс контакта, которого нужно удалить: '))
    return del_el

def get_search_element():
    search_el = input('Что будем искать?: ')
    return search_el

def show_find_results(filter_phone_book):
    if len(filter_phone_book) == 0:
        print('Элементы не найдены')
    else:
        for id, contact in enumerate(filter_phone_book):
            print(id, *contact)