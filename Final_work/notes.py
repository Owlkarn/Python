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
