import json
import datetime

# Функция для чтения заметок из файла
def read_notes():
    try:
        with open('notes.json', 'r') as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []
    return notes

# Функция для записи заметок в файл
def write_notes(notes):
    with open('notes.json', 'w') as f:
        json.dump(notes, f)

# Функция для добавления новой заметки
def add_note():
    notes = read_notes()
    if not notes:
        last_id = 0
    else:
        last_id = notes[-1]['id']
    new_id = last_id + 1
    title = input('Введите заголовок заметки: ')
    body = input('Введите текст заметки: ')
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    note = {'id': new_id, 'title': title, 'body': body, 'date': date}
    notes.append(note)
    write_notes(notes)
    print(f'Заметка с id {new_id} добавлена')