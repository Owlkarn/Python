import controller

phone_book = []

def get_phone_book():
    global phone_book
    return phone_book


def open_file(path): 
    global phone_book
    phone_book = []
    with open (path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for item in data:
        contact = item.replace('\n', '').split(';')
        phone_book.append(contact)
    print(phone_book[0])

def new_contact(contact):
    global phone_book
    phone_book.append(list(contact))

def change_contact(id, choise, value):
    global phone_book
    phone_book [int(id)][int(choise)] = value

def prepare_data_to_write(data):
    new_data = [data[n][0]+';'+data[n][1]+';'+data[n][2]+'\n' for n in range(len(data))]
    return new_data
    
def save_phone_book(path):
    global phone_book
    new_phone_book = prepare_data_to_write(phone_book)
    with open (path, 'w', encoding='UTF-8') as data:
        data.writelines(new_phone_book)

def del_element(number):
    global phone_book
    phone_book.pop(number)