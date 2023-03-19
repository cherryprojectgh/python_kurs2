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
        pass

ini = ini_file(r'C:\Users\Bartek\Documents\Python\pliki\my.ini')
ini.write_param('version', 1)
ini.write_param('level','advanced')
ini.save_on_disk()

ini2 = ini_file(r'C:\Users\Bartek\Documents\Python\pliki\my.ini')
print(ini2.params)
print(ini2.read_params('version'))
print(ini2.read_params('level'))

print('-'*100)

with ini_file(r'C:\Users\Bartek\Documents\Python\pliki\my.ini') as ini3:
    print(ini3.params)
    print(ini3.read_params('version'))
    print(ini3.read_params('level'))

# -----------------------------------------------------------------------------------------

# https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip

url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip'
path = r'C:\Users\Bartek\Documents\Python\pliki\euroxref.zip'

class zip_from_web:

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def __enter__(self):
        response = requests.get(self.url)
        with open(self.path, 'w') as file:
            file.write(response.content)
            
        return self
    
    def __exit__(self):
        pass

with zip_from_web('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'c:/temp/euroxref.zip') as f:
 
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir('c:/temp')
        z.extract(a_file, '.', None)