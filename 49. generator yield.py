import datetime as dt

def million_days(year, month, day, maxdays):
    date = dt.date(year, month, day)

    for element in range(maxdays):
        yield(date + dt.timedelta(days=element))

for element in million_days(2000,1,1,3):
    print(element)

# ------------------------------------------------------

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
            self.current_product =0
            raise StopIteration()
 
        item_to_return = "{} - {} -{}".format(self.products[self.current_product],
                                              self.promotions[self.current_promotion],
                                              self.customers[self.current_customer])
 
        self.current_customer += 1
 
        return  item_to_return
 
    def __iter__(self):
        return  self
 
 
products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 2)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]
 
combinations = Combinations(products, promotions, customers)
 
for c in combinations:
    print(c)



#generator

def combinations_generator(products, promotions, customers):
    for product in products:
        for promo in promotions:
            for customer in customers:
                yield('{} - {} - {}'.format(product,
                                            promo,
                                            customer))
                
products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 2)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]

for element in combinations_generator(products, promotions, customers):
    print(element)