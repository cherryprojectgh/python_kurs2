'''class BITException(Exception):
    
# text - treść komunikatu błędu
# area - miejsce wystąpienia błędu

    def __init__(self, text, area):
        super().__init__(text)
        self.area = area

    def __str__(self):
        return '\nBłąd: {}\nDodatkowy opis: {}\n'.format(super().__str__(), self.area)

class BITSecurityException(BITException):
    pass

class BITDataFormatException(BITException):
    pass


try:
    raise BITSecurityException('file format is incorrect','finnacial data')

except BITSecurityException as error:
    print('Application Security error: {}'.format(error))

except BITDataFormatException as error:
    print('Application data malformed error: {}'.format(error))

except BITException as error:
    print('Application error: {}'.format(error))

except Exception as error:
    print('General error: {}'.format(error))'''

# -----------------------------------------------------------------------------------

import datetime as dt
 
class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
 
    def check_data(self):
        if len(self.title) == 0:
            raise TripNameException("Title is empty!")
        if self.start > self.end:
            raise TripDateException("Start date is later than end date!")
 
    @classmethod
    def publish_offer(cls, trips):
 
        list_of_errors = []
 
        for trip in trips:
            print('Sprawdzam: ', trip.symbol)
            try:
                trip.check_data()

            except TripNameException as error:
                list_of_errors.append(error)
                print(error)

            except TripDateException as error:
                list_of_errors.append(error)
                print(error)
                
            except Exception as error:
                list_of_errors.append(error)
                print(error)
        
        if len(list_of_errors) > 0:
            raise TripException('The list of trips has errors',list_of_errors)
        else:
            print('the offer will be published...')
        
class TripException(Exception):

    def __init__(self, text, description):
        super().__init__(text)
        self.description = description
    
    def __str__(self):
        return '>>>Text: {}\n>>>Description: {}'.format(super().__str__(), self.description)

class TripNameException(TripException):

    def __init__(self, text):
        super().__init__(text, 'Name of the trip is missing. You need to name the trip somehow...')

class TripDateException(TripException):

    def __init__(self, text):
        super().__init__(text, 'The dates are incorrect. The starting date should be earlier than the ending date...')



trips = [
            Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
            Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
            Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
        ]
 
try:
    print('#'*60)
    print('Publishing trips...')
    Trip.publish_offer(trips)
    print('... done')
except TripException as error:
    print('--- Podsumowanie ---')
    print('THERE ARE ERRORS')
    print(error)
    print('THE OFFER CANNOT BE PUBLISHED')