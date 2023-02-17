import os

print()

file_path = "C:\\Temp\\data_input\\test.123.txt"

def number_of_words(file_path):
    file = open(file_path, 'r', encoding="utf-8")
    file_content = file.read()
    file.close()

    return len(file_content.split(' '))

# uproszczona wersja zapisu IF
path_exist = os.path.isfile(file_path) and print(number_of_words(file_path))


