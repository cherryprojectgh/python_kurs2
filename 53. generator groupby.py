import itertools as it
import os

data = []
path = r"D:\PROJEKTY\Python\PLIKI\data.txt"

with open(path,'r',encoding='utf') as file:
    for line in file:
        row = line.rstrip('\n').split(':')
        temp = {'type' : row[0], 'action' : row[1]}
        data.append(temp)

print(data)

data = sorted(data, key = lambda x: x['type'])

for key, other in it.groupby(data, key = lambda x: x['type']):
    # print('The key is {} and the group is {}'.format(key, list(other)))
    print('The key is {} and the number is {}'.format(key, len(list(other))))

# ---------------------------------------------------------------------------

def scantree(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            yield entry
            yield from scantree(entry.path)
        else:
            yield entry
 
listing = scantree('C:/temp')
for l in listing:
    print('DIR ' if l.is_dir() else 'FILE', l.path)
 
 
listing = scantree('C:/temp')
listing = sorted(listing, key=lambda e: e.is_dir())
 
for is_dir, elements in it.groupby(listing, key=lambda e: e.is_dir()):
    print('DIR ' if is_dir else 'FILE', len(list(elements)))