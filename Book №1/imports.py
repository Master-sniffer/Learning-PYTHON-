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


