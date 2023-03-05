'''
print('-'*100)

def process_invoice(netto, brutto):
    if netto >= brutto:
        raise ValueError('Netto should be lower or equal to brutto')
    else:
        print('Proccesing invoice: netto={} brutto={}'.format(netto, brutto))

netto = 1230
brutto = 100

try:
    process_invoice(netto, brutto)

except ValueError as error:
    print('The volume on invoice are incorrect: {}'.format(error))

except Exception as error:
    print('Error procesing invoice: {}'.format(error))'''

# -----------------------------------------------------------------------------

import datetime as dt
 
class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
 
    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Tytuł wycieczki jest pusty")
        if self.start > self.end:
            raise ValueError("Start wycieczki jest po dacie zakończenia wycieczki")
        
    @classmethod
    def publish_offer(cls, listOfTrips):
        listOfErrors = []

        for element in listOfTrips:

            try:
                print('>>> Sprawdzam: {}'.format(element.symbol))
                element.check_data()

            except ValueError as error:
                print(error)
                listOfErrors.append('{} : {}'.format(element.symbol, error))

            except Exception as error:
                print(error)
                listOfErrors.append('{} : {}'.format(element.symbol, error))
        
        if len(listOfErrors)>0:
            raise Exception('Lista wycieczek zawiera kilka błędów: {}'.format(listOfErrors))
        else:
            print('Gra gitara')


trips = [
            Trip('IT-VNC', 'Italy-Venice',    dt.date(2023, 6, 1),  dt.date(2023, 6, 12)),
            Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
            Trip('IT-ROM', 'Italy-Rome',      dt.date(2023, 6, 21), dt.date(2023, 6, 12))
        ]


try:
    print('Rozpoczynam dodawanie wycieczek\n')
    Trip.publish_offer(trips)
    print('Done')
except Exception as error:
    print(error)
