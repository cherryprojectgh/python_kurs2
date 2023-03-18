import time
import html

class time_measure:

    def __init__(self):
        pass

    def __enter__(self):
        print('entering...')
        self.__start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tp):
        print('exiting....')
        self.__stop = time.time()
        self.__difference = self.__stop - self.__start
        print('Execition time: {}'.format(self.__difference))

with time_measure() as myTimer:
    time.sleep(3)

# ----------------------------------------------------------------------

print('-'*100)

class HtmlCM:

    def __init__(self):
        pass

    def __enter__(self):
        print('<TABLE>')
        print('     <TR')
        print('         <TH>Number</TH><TH>Description</TH>')
        print('     </TR>')

    def __exit__(self):
        print('</TABLE>')

with HtmlCM() as html:
    print('         <TR>')
    print('             <TD>1</TD><TD>Say hello!</TD>')
    print('         </TR>')
    print('         <TR>')
    print('             <TD>1</TD><TD>Say good bye!</TD>')
    print('         </TR>')
