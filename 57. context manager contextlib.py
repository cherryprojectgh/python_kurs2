import os
import zipfile
import requests
import contextlib

class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def download_file(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self
    
    def close(self):
        os.remove(self.tmp_file)

with contextlib.suppress(FileNotFoundError):

    with contextlib.closing(FileFromWeb('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'C:/Users/Bartek/Documents/Python/pliki/dupa.zip')) as f:

        f.download_file()

        with zipfile.ZipFile(f.tmp_file, 'r') as z:
            a_file = z.namelist()[0]
            print(a_file)
            os.chdir('C:/Users/Bartek/Documents/Python/pliki')
            z.extract(a_file,'.',None)

        os.remove(f.tmp_file)
