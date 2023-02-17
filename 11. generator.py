list_A = list(range(6))
list_B = list(range(6))

gen = ((a,b) for a in list_A for b in list_B if a % 2 == 1 and b % 2 == 0 )
print(gen) 

print(next(gen))
print(next(gen))

print('-'*30)

for _ in gen:
    print(_)

print('-'*30)

for _ in gen:
    print(_)

while True:
    try:
        print(next(gen))
    except StopIteration:
        print('all values have been generated')
        break

#generator zwraca wartość tylko 1 raz

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
 
routes = ( (start, stop) for start in ports for stop in ports)
 
counter=0
for (start, stop) in routes:
    print("{} - {}".format(start, stop))
    counter+=1
          
print(counter)
 
##########
 
routes = ( (start, stop) for start in ports for stop in ports if start != stop)
 
counter=0
for (start, stop) in routes:
    print("{} - {}".format(start, stop))
    counter+=1
          
print(counter)
 
##########
 
routes = ( (start, stop) for start in ports for stop in ports if start < stop)
 
counter=0
for (start, stop) in routes:
    print("{} - {}".format(start, stop))
    counter+=1
          
print(counter)