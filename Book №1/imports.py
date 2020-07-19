#Here will be published imports from the Book 1. Number of the line where i used this import, will be provided

##Line 1255
def make_pizza(size, *toppings):
    print (f"The size of that baby is {size} and toppings are: ")
    for i in toppings:
        print (i)


        
##Line 1289
def print_models(unprinted,completed):
    while unprinted:
        current=unprinted.pop()
        print (f"{current} is in progress")
        completed.append(current)

def show_models(completed):
    for i in completed:
        print (i)



##1741
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometr= 0 #giving atributes by the default
    
    def desryption (self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_metr(self):
        print (f"This car has {self.odometr} on it")
    
    def update_odom(self,mile):
        if mile >self.odometr:
            self.odometr=mile
        else:
            print ("You can't roll back the odometr")
    
    def increasement(self,miles):
        self.odometr+=miles
    
    def fill_gas_tank(self,nub):
        self.odometr+=nub
class Battery():
    def __init__(self,battery=75):
        self.battery=battery
    
    def describe_battery(self):
        print ("That's how much juice left - ",self.battery)
    
    def get_range(self):
        if self.battery==75:
            range=260
        elif self.battery==100:
            range=315
        print (f"This car can go this far with this fuel {range}")
    
    def upgrade_Battery(self):
        if self.battery!=100:
            self.battery=100

class Electric_car(Car): 

    def __init__(self,make,model,year):
        super().__init__(make,model,year)        
        self.battery=Battery()#Здесь изменили 
    
    def fill_gas_tank(self,nub):
        print ("This type of car doesn't need it !")


##1806
class Restaurant():

    def __init__ (self,name,cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
        self.flavours=["Vanilla", "mango", "raspberry", "chocolate"]
    
    def ice_cream_stand (self):
        print ("\nKinds of ice-cream: ")
        for i in self.flavours:
            print (i)
    
    def desctibe (self):
        print (self.name)
        print (self.cuisine_type)
    
    def open_restaurant(self):
        print ("Restaurant is open now")


##1813
class User:

    def __init__(self):
        print("\nhello , admin\n")

    def first_name(self,name=None):
        self.name=name
        return (self.name)
    
    def last_name(self,l_name=None):
        self.l_name=l_name
        return l_name
    
    def info (self,*args):
        self.args=args
    
    def describe_user(self):
        print (f"Hello {self.name} {self.l_name} i know so much about you, for example: ")
        for i in self.args:
            print(i)

class Privileges():
    def __init__(self,privileges="Can add users, can deleate users, can ban userss" ):
        self.privileges=privileges
    
    def show_privileges (self):
        print (self.privileges)

class Admin(User):

    def __init__(self):
        self.admin=Privileges()
