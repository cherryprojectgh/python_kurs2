
def calculate(kind='+', *args):
    result = 0
    if kind == '+':
        for element in args:
            result += element
    elif kind == '-':
        for element in args:
            result -= element
    return result

print(calculate('+',1,2,3))
print(calculate('-',1,2,3))

def create_function(kind = '+'):
    source = '''
def f(*args):
    result = 0
    for element in args:
        result {}= element
    return result
''' .format(kind)

    exec(source, globals())

    return f

f_add = create_function('+')
print(f_add(1,2,3,4))
f_subs = create_function('-')
print(f_subs(10,20,30))

#-------------------------------------------------------

from datetime import datetime

start = datetime(2019,1,1,0,0,0)
end = datetime.now()

def time_span_m(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 60)[0]

def time_span_h(start, end):
    duration = end - start
    duration_in_h = duration.total
    return divmod(duration_in_s, 3600)[0]

def time_span_d(start, end):
    duration = end - start
    duration_in_d = duration.total
    return divmod(duration_in_s, 86400)[0]



def create_function2(span):
    sec = 60 if span == 'm' else 3600 if span == 'h' else 86400 
    
    source2 = '''    
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]
'''.format(sec)
    exec(source2, globals())

    return f

f_minutes = create_function2('m')
f_hours = create_function2('h')
f_days = create_function2('d')

print(f_minutes(start, end))
print(f_hours(start, end))
print(f_days(start, end))


