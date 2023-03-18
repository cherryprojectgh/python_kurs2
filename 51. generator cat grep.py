import os
import requests

path = r'D:\PROJEKTY\Python\PLIKI'
searchString = 'dupa'
fileExtension = '.py'


def gen_get_files(dir):
    for file in os.listdir(dir):
        yield os.path.join(dir, file) # D:\PROJEKTY\Python\PLIKI\plik1.txt
                        
def gen_get_file_lines(filename):
    with open(filename, 'r', encoding='utf8') as f:
        for line in f.readlines():
            yield line.replace('\n', '')

def check_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False
    
for file in gen_get_files(path): # D:\PROJEKTY\Python\PLIKI\plik1.txt
    for line in gen_get_file_lines(file): # zwraca adres z pliku otworzonego ze zwrócnej ścieżki
        print('plik - {} - {}'.format(line, check_webpage(line)))









# def generate_files(baseDir, fileExtension):
#     print('funkcja start')
#     for dirName, subdires, fileNames in os.walk(baseDir):
#         for fileName in fileNames:
#             if fileName.endswith(fileExtension):
#                 fullFileName = os.path.join(dirName, fileName)
#                 #rint(fullFileName)
#                 yield fullFileName


# def grep_files(searchString, files):
#     for file in files:
#         with open(file, encoding='utf8') as text:
#             if searchString in text.read():
#                 yield file

# filesGenerator = generate_files(path, fileExtension)

# for file in grep_files(searchString, filesGenerator):
#     print(file)

# # ----------------------------------------------------------------

# def gen_get_files(dir):
#     files = os.listdir(dir)

