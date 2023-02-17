list_A = list(range(6))
list_B = list(range(6))

print(list_A, list_B)

product = []

for a in list_A:
    for b in list_B:
        product.append((a,b))
print(product)

#tworże listę z tupletem a,b - a jest pobierany z listy list_A a b z listy list_B
product = [(a,b) for a in list_A for b in list_B]
print(product)

product = [(a,b) for a in list_A for b in list_B if a % 2 == 1 and b % 2 == 0 ]
print(product) 

product = {a:b for a in list_A for b in list_B if a % 2 == 1 and b % 2 == 0 }
print(product) 

numbers = list(range(1,10))
print(numbers)


#------------------------------------------------------------------------------------

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

ports_all = [(a,b) for a in ports for b in ports if b != a]
print(ports_all)

