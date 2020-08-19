
#==========================================
# Purpose: An object of this class represents a complex number, in the form a + bi
# Instance variables: real = real number (the a in a + bi); imag = imaginary number (the b in a + bi)
# Methods:
#   __init__ = constructor that initializes the variables - real and imag
#   get_real = returns the value of the real number
#   get_imag = returns the value of the imaginary number
#   set_real = sets the value of the real number to a new real number
#   set_imag = sets the value of the imaginary number to a new imaginary number
#   __str__ = overloads the __str__ method to place real and imaginary in proper form - a + b
#   __add__ = overloads the addition method to add two complex numbers
#   __mul__ = overloads the multipication method to multiply two complex numbers
#   __eq__ = overloads the equals method to determine whether two Complex objects are equal
#==========================================


class Complex:
    def __init__(self,real=0,imag=0):
        self.real = real
        self.imag = imag
    def get_real(self):
        return self.real
    def get_imag(self):
        return self.imag
    def set_real(self, new_real):
        self.real = new_real
    def set_imag(self, new_imag):
        self.imag = new_imag
    def __str__(self):
        return str(self.real) + ' + ' + str(self.imag) + 'i'  
    def __add__(self, other):
        return Complex((self.get_real() + other.get_real()), (self.get_imag() + other.get_imag()))
    def __mul__(self, other):
        a = (self.get_real() * other.get_real()) - (self.get_imag() * other.get_imag())
        b = (self.get_real() * other.get_imag()) + (self.get_imag() * other.get_real())
        return Complex(a, b)
    def __eq__(self, other):
        if (self.get_real() == other.get_real()) and (self.get_imag() == other.get_imag()):
            return True
        else:
            return False

#==========================================
# Purpose: An object of this class represents an item of clothing
# Instance variables:
#   name = string describing what the item is called
#   price = float describing the item’s price in USD
#   category = string that describes where the item is worn. It must be one of four values: 'Head', 'Torso', 'Legs', or 'Feet'.
#   store = string that describes the name of the store where the item can be found
# Methods:
#   __init__ = constructor that initializes the instance variables - name, price, category, and store
#   __str__ = overloads the __str__ method to print the Item object in form name, category, store: $price
#   __lt__ = overloads the "less than" method to determine whether an Item object is less than another Item object by comparing its price
#==========================================

class Item:
    def __init__(self, name='', price=0.0, category='', store=''):
        self.name = name
        self.price = price
        self.category = category
        self.store = store
    def __str__(self):
        return self.name + ', ' + self.category + ', ' + self.store + ': $' + str(self.price)
    def __lt__(self, other):
        if self.price < other.price:
            return True
        else:
            return False

#==========================================
# Purpose: An object of this class represents a store with Item objects
# Instance variables:
#   name = string, representing the name of the store
#   items = list of Item objects, representing every item in the store’s inventory
# Methods:
#   __init__ = constructor that initializes the instance variables - name and filename
#   __str__ = overloads the __str__ method to print all the Item objects with a line separating each object
#==========================================

class Store:
    def __init__(self, name='', filename=''):
        self.name = name
        fp = open(filename, 'r')
        contents = fp.readlines()
        contents.pop(0)
        items = []
        for line in contents:
            line = line.split(',')
            line[2] = line[2].split('\n')
            items.append(Item(line[0],float(line[1]),line[2][0], self.name))
            line[2] = ' '.join(line[2])
            line = ','.join(line)
        self.items = items
        fp.close()
    def __str__(self):
        store = self.name + '\n'
        for elem in self.items:
            if elem != self.items[-1]:
                store+= str(elem) + '\n'
            else:
                store+= str(elem)
        return store

def cheap_outfit(store_list):
    cheapest_outfit = {}
    head = []
    legs = []
    feet = []
    torso = []
    for store in store_list:
        for i in range(len(store.items)):
            if store.items[i].category == 'Head':
                head.append(store.items[i])
            elif store.items[i].category == 'Legs':
                legs.append(store.items[i])
            elif store.items[i].category == 'Feet':
                feet.append(store.items[i])
            elif store.items[i].category == 'Torso':
                torso.append(store.items[i])
    cheapest_outfit.update({'Head': min(head)})
    cheapest_outfit.update({'Torso': min(torso)})
    cheapest_outfit.update({'Legs': min(legs)})
    cheapest_outfit.update({'Feet': min(feet)})

    return cheapest_outfit
                    

















        
