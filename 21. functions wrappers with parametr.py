import datetime
import functools
import os

log_file_path_salary = r'D:\PROJEKTY\Python\PLIKI\log_change_salary.txt'
log_file_path_position = r'D:\PROJEKTY\Python\PLIKI\log_change_position.txt'

def create_function_with_wrapper_log_file(log_file_path):
    def create_function_with_wrapper(func):
        def func_with_wrapper(*args, **kwargs):
            file = open(log_file_path, 'a')
            file.write('-'*20 + '\n')
            file.write('Logs for function: {} \n'.format(func.__name__))
            file.write('Following arguments were used: \n')
            file.write(' '.join('{}'.format(x) for x in args)) #połączenie wszystkich argumentów w jednego stringa
            file.write('\n')
            file.write(' '.join('{}={}'.format(k,v) for k, v in kwargs.items()))
            file.write('\n')
            file.write('Function sterted at {} \n'.format(datetime.datetime.now().isoformat()))
            result = func(*args, **kwargs) #wywołanie śledzonej funkcji
            file.write('Function ended at {}'.format(datetime.datetime.now().isoformat()))
            file.write('\n')
            file.write('Function returned {}'.format(result))
            file.write('\n')
            file.write('-'*20)
            file.close()
            return result #wynik śledzonej funkcji
        return func_with_wrapper
    return create_function_with_wrapper     


@create_function_with_wrapper_log_file(log_file_path_salary) 
def change_salary(emp_name, new_salary, is_bonus = False):
    print('CHANGING SALARY FOR {} TO {} AS BONUS={}'.format(emp_name, new_salary, is_bonus))
    return new_salary

print(change_salary('Johnson', 20000, True))

@create_function_with_wrapper_log_file(log_file_path_position) 
def change_position(emp_name, new_position, is_bonus = False):
    print('CHANGING POSITION FOR {} TO {} AS BONUS={}'.format(emp_name,new_position,is_bonus))
    return new_position

print(change_position('Johnson', 'Manager', True))       

#---------------------------------------------------------------------------------------------ZADANIE

# Action FILE_CREATE executed on c:\temp\dummy_file.txt on 2029-01-12 9:29:17
# Action FILE_DELETE executed on c:\temp\dummy_file.txt on 2029-01-12 9:33:18
# Action FILE_CREATE executed on c:\temp\dummy_file.txt on 2029-01-12 9:39:57
# Action FILE_DELETE executed on c:\temp\dummy_file.txt on 2029-01-12 9:44:18

file_path_log = r'D:\PROJEKTY\Python\PLIKI\log_file.txt'

def create_f_with_wrapper_log_file(log_file_path):
    def create_f_with_wrapper(func):
        def f_with_wrapper(path):
            file = open(log_file_path,'a')
            file.write('Action {} executed on {} on {} \n'.format(func.__name__, path,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            file.close()
            result = func(path)
            return result
        return f_with_wrapper
    return create_f_with_wrapper

@create_f_with_wrapper_log_file(file_path_log)
def create_file(path):
    print('creating file {}'.format(path))
    open(path,'w+')

@create_f_with_wrapper_log_file(file_path_log) 
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)
 

create_file(r'D:\PROJEKTY\Python\PLIKI\dummy_file.txt')
delete_file(r'D:\PROJEKTY\Python\PLIKI\dummy_file.txt')
create_file(r'D:\PROJEKTY\Python\PLIKI\dummy_file.txt')
delete_file(r'D:\PROJEKTY\Python\PLIKI\dummy_file.txt')
