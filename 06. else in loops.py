print()

'''
instruction = ['say hello', 'abort', 'say how are you', 'ask for money', 'say thank you', 'say bye']
instruction_approved = []

for instr in instruction:
    print('Adding instruction:', instr)
    instruction_approved.append(instr)

    if instr == 'abort':
        print('Aborting!!!')
        instruction_approved.clear()
        break

else:
    print('Following actions will be taken:', instruction_approved)
'''

import os
import sys
import urllib.request

data_dir = r'C:\Temp\data_input'
pages = [
    {'name':'onet', 'url':'http://onet.pl'},
    {'name':'wp', 'url':'http://wp.pl'},
    {'name':'interia', 'url':'http://interia.pl'},
    {'neme':'interia', 'url':'http://interia.pl'},
]

for item in pages:
    try:
        file_name = '{}.html'.format(item['name'])
        path = os.path.join(data_dir, file_name)

        print('Zapisuje stronę: %s do pliku %s' % (item['url'], file_name))
        urllib.request.urlretrieve(item['url'],path)
        print('Strona %s została zapisana' % item['name'])
    except:
        print('Coś poszło nie tak: %s' % sys.exc_info()[0])    
else:
    print('Zapisywanie zakończone')

