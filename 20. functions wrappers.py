
#wrapper służy do monitorowania przebiegu innych funkcji

import datetime
import functools

def create_function_with_wrapper(func):
    def func_with_wrapper(*args, **kwargs):
        print('-'*20)
        print('Following arguments were used:',args)
        print('Function "{}" sterted at {}'.format(func.__name__, datetime.datetime.now().isoformat()))
        result = func(*args, **kwargs) #wywołanie śledzonej funkcji
        print('Function ended at {}'.format(datetime.datetime.now().isoformat()))
        print('Function returned {}'.format(result))
        print('-'*20)
        return result #wynik śledzonej funkcji
    return func_with_wrapper 


@create_function_with_wrapper
def change_salary(emp_name, new_salary, is_bonus = False):
    print('CHANGING SALARY FOR {} TO {} AS BONUS={}'.format(emp_name,new_salary,is_bonus))
    return new_salary

print(change_salary('Johnson', 20000, True))

#-----------------------------------------------------------------------------------------------

import time

def wrapper(function):
    def function_with_wrapper(*args, **kwargs):
        print('-'*20)
        print('Following arguments were used:',args)
        print('Function "{}" started.'.format(function.__name__))
        time_start = time.time()
        result = function(*args, **kwargs)
        time_end = time.time()
        time_elapsed = time_end - time_start
        print('Function lasted {}'.format(time_elapsed))
        return result
    return function_with_wrapper

@wrapper
def get_sequence(n):
    
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v

print(get_sequence(10))