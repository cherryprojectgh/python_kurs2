import os
import zipfile
import requests

class ini_file:

    def __init__(self, path):
        self.path = path
        self.params = {}
        self.read_from_disk()

    def read_from_disk(self):
        if os.path.isfile(self.path):
            with open(self.path, encoding='utf8') as file:
                for line in file:
                    parts = line.replace('\n', '').split('=')
                    self.params[parts[0]] = parts[1]

    def read_params(self, key):
        if key in self.params.keys():
            return self.params[key]
        else:
            return None

    def write_param(self, key, value):
        self.params[key] = value

    def save_on_disk(self):
        with open(self.path, 'w') as file:
            for key, value in self.params.items():
                line = '{}={}\n'.format(key, value)
                file.write(line)
            
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('-'*100)
        print('__exit__')
        print('exc_type = {}'.format(exc_type))
        print('exc_val = {}'.format(exc_val))
        print('exc_tb = {}'.format(exc_tb))
        print('-'*100)
        if exc_type == OSError:
            return False
        else:
            return True

with ini_file(r'C:\Users\Bartek\Documents\Python\pliki\my.ini') as ini:
    ini.write_param('mode','strict')
    ini.write_param('loglevel','light')
    ini.save_on_disk()
    print(10/0)

# ------------------------------------------------------------------------------------
dupa = 123
class zip_from_web:

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def __enter__(self):
        response = requests.get(self.url)
        with open(self.path, 'w') as file:
            file.write(response.content)
            
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('>>>> Error details', exc_type, exc_val, exc_tb)
        if exc_type == KeyError:
            print('>> There is no file in archive! {}'.format(exc_val))
            return True
        elif exc_type == FileNotFoundError:
            print('>> Incorrect directory/file: {}'.format(exc_val))
            return True
        else:
            return False

with zip_from_web('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'c:/temp/euroxref.zip') as f:
 
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir('c:/temp')
        z.extract(a_file, '.', None)