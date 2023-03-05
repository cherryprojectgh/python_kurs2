clients = {
    'Info'  : 0.5,
    'DATA'  : 0.2,
    'SOFT'  : 0.2,
    'INTER' : 0.1,
    'OMEGA' : 0.0
}

#myClient = input('Enter client\' name: ')
totalCost = 7200

try:
    print('The % ratio for {} is {}'.format(myClient, clients[myClient]))
except Exception as e: #instancja klasy expect
    print('Sorry we have an error...\nDetails: {}'.format(e))
else:
    print('The cost for {} is {}'.format(myClient, clients[myClient]* totalCost))
finally:
    print('-= Calculation finished =-')

# ------------------------------------------------------------------------------------------------

print('-'*100)

import requests
import os
import shutil
 
def save_url_to_file(url, file_path):
        
    r = requests.get(url, stream = True)     
    with open(file_path, "wb") as f: 
        f.write(r.content)
 
url = 'http://www.mobilo24.eu/spis/'
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

except Exception as e:
    print('\n>>> error')
    print('Huston, mamy problem...\nURL: {}\nSzczegóły: {}'.format(tmpfile_path, e))
    print('>>> error\n')

else:
    print('Wszystko ładnie pykło')

finally: 
    os.remove(tmpfile_path)
    print('KONIEC')