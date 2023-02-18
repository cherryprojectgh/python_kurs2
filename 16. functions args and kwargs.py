#zmienna z gwiazdką daje możliwość wprowadzenia większej liczby argumentów które tworzą listę
#zmienna z dwoma gwiazdkami argument poprzedzony słowem kluczowym które tworzą słownik

def buy_me (prefix='Please buy me', what='something nice', *args, **kwargs):
    print(prefix, what)
    print(args)
    print(kwargs)

products = ['milk','bread','flakes']
parameters = {'price':'low', 'time':'now'}

buy_me('Buy me', 'newspaper', *products, **parameters)

#---------------------------------------------------------------------------------------------

def calculate_paint(efficency_ltr_per_m2, *args):
    for element in args:
        wynik = efficency_ltr_per_m2 * element
    return wynik

print(calculate_paint(2, 10, 20))

m2 = [10,20,22,79]

print(calculate_paint(2,*m2))

#---------------------------------------------------------------------------------------------

file_path = r'D:\PROJEKTY\Python\PLIKI\dupa.txt'

def log_it(*args):
    t = ' '.join(args)
    file = open(file_path,'a')
    file.write(t)
    file.write('\n')
    file.close()

log_it('Starting procesing forcasting')
log_it('ERROR','Not enough data','invoices','2020')

print('koniec')