clients = {
    'INFO'  : 0.5,
    'DATA'  : 0.2,
    'SOFT'  : 0.2,
    'INTER' : 0.1,
    'OMEGA' : 0.0
}

myClient = input('Enter client\' name: ')
totalCost = 7200

try:
    ratio = float(input('Enter new ratio: '))
    print('The % ratio for {} is {}, a new one is {}'.format(myClient, clients[myClient], ratio))
    print('The cost for {} is {}'.format(myClient, ratio * totalCost))
    print('The new ratio in comperison to old ratio: {}'.format(clients[myClient]/ratio))

except KeyError as e:
    print('Client {} is not on the list {}.\n>>> Details: {}'.format(myClient, [clients for clients in clients.keys()], e))

except (ValueError, ZeroDivisionError) as error:
    print('There is a problem with entered value for ratio - it must be a number greater than 0.\n>>> Details: {}'.format(error))

#except ZeroDivisionError as error:
#    print('The new ratio cannot be 0.\n>>> Details: {}'.format(error))

except Exception as e: #instancja klasy expect
    print('Sorry we have an error...\n>>> Details: {}'.format(SystemError()))

# ----------------------------------------------------------------------------------------------------------------

print('-'*100)

import sys
import requests
import os
import shutil
 
def save_url_to_file(url, file_path):
        
    r = requests.get(url, stream = True)     
    with open(file_path, "wb") as f: 
        f.write(r.content)
 
url = 'http://dupa-opil.pl'
#url = 'http://www.mobilo24.eu/spis/'
dir = r'D:\PROJEKTY\Python\PLIKI'
tmpfile = 'download.tmp'
file = 'spis.html'
 
tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

print('tmpfile_path: ', tmpfile_path)
print('file_path: ', file_path )
print('-'*100)

try:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
    
    save_url_to_file(url, tmpfile)
    shutil.copy(tmpfile_path, file_path)

except requests.exceptions.ConnectionError as error:
    print('Nieprawidłowy adres URL.\n>>> Szczegóły błędu:\n{}'.format(error))

except (PermissionError, FileNotFoundError) as error:
    print('Brak dostępu do pliku.\n>>> Szczegóły błędu:\n{}'.format(error))

except Exception as e:
    print('\n>>> error')
    print('Huston, mamy problem...\nURL: {}\nSzczegóły: {}\n{}'.format(tmpfile_path, e, sys.exc_info()))
    #traceback.print_exc()
    print('>>> error\n')


