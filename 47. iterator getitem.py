'''import datetime as dt

class MillionDays:

    def __init__(self, year, month, day, maxdays):
        self.date = dt.datetime(year, month, day)
        self.maxdays = maxdays

    def __getitem__(self, item):
        if item <= self.maxdays:
            return self.date + dt.timedelta(days=item)
        else: raise StopIteration

md = MillionDays(2000,1,1,2500000)

it = iter(md)

print(md[0], md[1], md[2], md[10])

print(next(it))
print(next(it))
print(next(it))
'''
# ---------------------------------------------------------------------------

class Combinations:
 
    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers
 
    def __getitem__(self, item):

        if item >= len(self.products) * len(self.promotions) * len(self.customers):
            raise StopIteration()
        else:
            pos_products = item // (len(self.promotions) * len(self.customers))
            item = item % (len(self.promotions) * len(self.customers))

            pos_promotions = item // len(self.customers)
            item = item % len(self.customers)

            pos_customers = item

        return '{} - {} - {}'.format(self.products[pos_products],
                                     self.promotions[pos_promotions],
                                     self.customers[pos_customers])
 
   
products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]
 
combinations = Combinations(products, promotions, customers)

# for element in range(0,31):
#    print(element, combinations[element])

combinations_iterator = iter(combinations)
print(next(combinations_iterator))
 
for c in combinations_iterator:
    print(c)