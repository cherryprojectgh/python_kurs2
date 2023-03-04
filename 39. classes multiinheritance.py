class Car:

    def __init__(self, brand, model, isOnSale):
        print('>> Class Car - init - starting')
        self.brand = brand
        self.model = model
        self.isOnSale = isOnSale
        self.name = '{}  {}'.format(brand, model)
        print('>> Class Car - init- finishing')

    def get_info(self):
        print('>> Class Car - get_info - starting')
        super().get_info()
        print('{} {}'.format(self.brand, self.model).upper())
        print('IS ON SALE        {}'.format(self.isOnSale))
        print('>> Class Car - get_info - stopping')

class Specialist:

    def __init__(self, firstName, lastName, brand):
        print('>> Class Specialist - __init__ - starting')
        self.firstName = firstName
        self.lastName = lastName
        self.name = '{} {}'.format(firstName, lastName)
        self.brand = brand
        print('>> Class Specialist - __init__ - finishing')

    def get_info(self):
        print('Class Specialist - get_info - starting')
        print('{} {} - ({})'.format(self.firstName, self.lastName, self.brand))
        print('Class Specialist - get_info - finishing')

class CarSpecialist(Car, Specialist):

    def __init__(self, brand, model, isOnSale, firstName, lastName):
        print('>> Class CarSpecialist - __init__ - starting')
        Car.__init__(self, brand, model, isOnSale)
        Specialist.__init__(self, firstName, lastName, brand.upper())
        print('>> Class CarSpecialist - __init__ - finishing')

    def get_info(self):
        print('>> Class CarSpecialist - get_info - starting')
        super().get_info()
        print('>> Class CarSpecialist - get_info - finishing')

tom = CarSpecialist('Toyota','Corolla',True,'Tom','Smith')
print(vars(tom))

tom.get_info()