'''import datetime
import sys

start = datetime.datetime.now()
print('Exceution started at: {}'.format(start))

# dates = [datetime.datetime(2000,1,1) + datetime.timedelta(days = i) for i in range(2500000)]
# print('size of dates is {}'.format(sys.getsizeof(dates)))
# for day in dates:
#    pass

class MillionDays:

    def __init__(self, year, month, day, maxdays):
        self.date = datetime.date(year, month, day)
        self.maxdays = maxdays

    def __next__(self):
        if self.maxdays <= 0:
            raise StopIteration()
        ret = self.date
        self.date += datetime.timedelta(days=1)
        self.maxdays -= 1
        return ret
    
    def __iter__(self):
        return self

md = MillionDays(2000,1,1,2500000)
print('size of MilionDay object is: {}'.format(sys.getsizeof(md)))
for d in md:
    pass


# md = MillionDays(2000,1,1,2500000)
# for i in range(2500000):
#     next(md)

stop = datetime.datetime.now()
print('Exceution ended at: {}'.format(stop))
print('Total time: {}'.format(stop - start))
'''

#-----------------------------------------------------------------------

class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0

    def __next__(self):
        if self.current_customer >= len(self.customers):
            self.current_customer = 0
            self.current_promotion += 1
        
        if self.current_promotion >= len(self.promotions):
            self.current_promotion = 0
            self.current_product += 1

        if self.current_product >= len(self.products):
            self.current_product = 0
            raise StopIteration
        
        item_to_return = '{} - {} - {}'.format(self.products[self.current_product], self.promotions[self.current_promotion], self.customers[self.current_customer])

        self.current_customer += 1

        return item_to_return
    
    def __iter__(self):
        return self


products = ["Product {}".format(i) for i in range(1, 500)]
#print(products)
 
promotions = ["Promotion {}".format(i) for i in range(1, 50)]
#print(promotions)
 
customers = ['Customer {}'.format(i) for i in range(1, 500)]
#print(customers)

combinations = Combinations(products,promotions,customers)

for element in combinations:
    print(element)
    pass

import time 
time.sleep(10)

