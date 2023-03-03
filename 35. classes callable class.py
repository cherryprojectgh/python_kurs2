class MemoryClass:

    def __init__(self, list):
        self.list_of_items = list

    def __call__(self, item):
        self.list_of_items.append(item)

mem = MemoryClass([])
print('List of items in memory', mem.list_of_items)

mem.list_of_items.append('buy sugar')
print('List of items in memory', mem.list_of_items)

mem('buy mil')
print('List of items in memory', mem.list_of_items)

#-----------------------------------------------------------
print('-'*60)

class NoDuplicates:

    def __init__(self, list):
        self.list_of_items = list

    def __Call__(self, new_items):
        for element in new_items:
            if element not in self.list_of_items:
                self.list_of_items.append(element)

my_no_dup_list = NoDuplicates(['keyboard','mouse'])
print(my_no_dup_list.list_of_items)

my_no_dup_list = NoDuplicates(['keyboard','mouse','pendrive'])
print(my_no_dup_list.list_of_items)

my_no_dup_list = NoDuplicates(['charger','pendrive'])
print(my_no_dup_list.list_of_items)