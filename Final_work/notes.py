import json
import datetime
import os

# Функция для чтения заметок из файла
def read_notes():
    try:
        with open('notes.json', 'r', encoding='utf-8') as f:
            notes = json.load(f)
    except FileNotFoundError:
        print('Заметок нет')
        notes = []
    return notes

# Функция для записи заметок в файл
def write_notes(notes):
    with open('notes.json', 'w', encoding='utf-8') as f:
        json.dump(notes, f, ensure_ascii=False)

# Функция для добавления новой заметки
def add_note():
    title = input('Введите заголовок заметки: ')
    body = input('Введите текст заметки: ')
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if not os.path.exists('notes.json'):
        with open('notes.json', 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False)

    with open('notes.json', 'r', encoding='utf-8') as f:
        notes = json.load(f)

    if not notes:
        id = 1  # если список заметок пуст, то устанавливаем id равным 1
    else:
        id = notes[-1]['id'] + 1  # иначе увеличиваем id на 1

    note = {'id': id, 'title': title, 'body': body, 'date': date}
    notes.append(note)

    with open('notes.json', 'w', encoding='utf-8') as f:
        json.dump(notes, f, ensure_ascii=False)

    print(f'Заметка с id {id} добавлена')

# Функция для вывода списка заметок
def list_notes():
    notes = read_notes()
    for note in notes:
        print(f'{note["id"]}. {note["title"]} ({note["date"]})')

# Функция для вывода заметки по идентификатору
def show_note():
    id = int(input('Введите id заметки: '))
    notes = read_notes()
    for note in notes:
        if note['id'] == id:
            print(f'Заголовок: {note["title"]}')
            print(f'Текст: {note["body"]}')
            print(f'Дата создания: {note["date"]}')
            return
    print('Заметка не найдена')

# Функция для редактирования заметки
def edit_note():
    id = int(input('Введите id заметки: '))
    notes = read_notes()
    for i in range(len(notes)):
        if notes[i]['id'] == id:
            title = input('Введите новый заголовок заметки: ')
            body = input('Введите новый текст заметки: ')
            date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            notes[i]['title'] = title
            notes[i]['body'] = body
            notes[i]['date'] = date
            write_notes(notes)
            print('Заметка отредактирована')
            return
    print('Заметка не найдена')

# Функция для удаления заметки
def delete_note():
    id = int(input('Введите id заметки: '))
    notes = read_notes()
    for i in range(len(notes)):
        if notes[i]['id'] == id:
            del notes[i]
            write_notes(notes)
            print('Заметка удалена')
            return
    print('Заметка не найдена')

# Функция для выборки заметок по дате
def filter_notes():
    date_str = input('Введите дату в формате ГГГГ-ММ-ДД: ')
    try:
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print('Некорректный формат даты')
        return
    notes = read_notes()
    filtered_notes = []
    for note in notes:
        note_date = datetime.datetime.strptime(note['date'], '%Y-%m-%d %H:%M:%S')
        if note_date.date() == date.date():
            filtered_notes.append(note)
        if filtered_notes:
            print(f'Заметки за {date_str}:')
            for note in filtered_notes:
                print(f'{note["id"]}. {note["title"]}')
        else:
            print(f'Заметки за {date_str} не найдены')

def main():
    while True:
        print('Выберите действие:')
        print('1. Список заметок')
        print('2. Добавить заметку')
        print('3. Просмотреть заметку')
        print('4. Редактировать заметку')
        print('5. Удалить заметку')
        print('6. Фильтр заметок по дате')
        print('7. Выход')
        choice = input()
        match choice:
              case '1':
                  list_notes()
              case '2':
                  add_note()
              case '3':
                  show_note()
              case '4':
                  edit_note()
              case '5':
                  delete_note()
              case '6':
                  filter_notes()
              case '7':
                  print('Выход из программы')
                  return
              case _:
                  print('Неправильный выбор, попробуйте еще раз!')

num_id = 0
main()