

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