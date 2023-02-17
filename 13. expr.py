var_x = 10
source = '''
new_var = 1
for i in range(var_x):
    print('-' * i)
    new_var += i
'''

result = exec(source)
print(result)

#exec wykonuje część kody i nie zwraca wartości

print(var_x)

#-------------------------------------------------------------------------------------------
import os

source_from_file = ''

files_to_process = [
    r"C:\Temp\data_input\skrypt1.py",
    r"C:\Temp\data_input\skrypt2.py"
    ]

print(len(files_to_process))

for file_path in files_to_process:
    print(os.path.basename(file_path))

    f = open(file_path, "r", encoding="utf-8")
    source_from_file = f.read()
    f.close()

    exec(source_from_file)