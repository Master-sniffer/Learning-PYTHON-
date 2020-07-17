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



##
