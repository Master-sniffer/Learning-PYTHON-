#import this # delete the first hashtag to see the truth

#deleting and inserting different stuff in list

baba = ["mama","papa","babu"]
message = f"my first anal was with\n\t{baba[1].title()}" # f перед ковычками дает нам возможность писать переменные в str формате, но только в спец скобочках {}
print (message)
baba.insert (1,"jui")
print (baba)
del baba[1]
print (baba)


#popping

poped_vary=baba.pop() #удалили последний элемент из списка
poped_vary1=baba.pop(1) # удалили элемент , который стоит на 1 месте (в списке - на 2)
print (baba)
print (poped_vary)
print (poped_vary1)
print (f"I really like my {poped_vary1.title()}\n\t so much")


#remove

kaag = ["mama","papa","babu","kaitu"]
kaag.remove("papa") #удалили элемент papa из этого списка ( и списков, которые могут быть ему равны !!!)
print (kaag)

kaag = ["mama","papa","babu","kaitu"]
print (kaag)
x="papa"
kaag.remove(x)
print (f"Well, sometimes some things happen, this is why i had to delete {x} , thats why i have now\n\t{kaag}")


#some additional tasks

guests = ["robert","Lusi","Karl","Mike","Piggy"]
for i in guests:
    print (i)
print (f"\n{guests[3]} cant come, cause he is ill\n")
guests[3]="Josh"
guests.append("Bill")
for i in guests:
    print (i)

print ("\nNew Guests\n")
guests.insert(0,"Clare")
guests.insert(4,"Michael")
for i in guests:
    print (i)


print ("\nremoving guests\n")
while (len(guests))>2:
    guests.pop() 
print (guests)
for i in guests:
    print (f"{i}, is still in list")

print ("\nDeleting each other\n")
while len(guests)!=0:
    del guests[0]

print (guests)


#sort

gadgets = ["telephone","Tesla","headphones","fridge","pip-boy"]
print (f"{gadgets} before sorting")
gadgets.sort() #сортируем их а алфавитном порядке
print (f"{gadgets} after sorting") 
gadgets.sort(reverse=True) #сортируем в реверсивном порядке - список наоборот 
print (f"{gadgets} after reverse sorting\n")


#sorted

gadgets = ["telephone","Tesla","headphones","fridge","pip-boy"]
print (f"{gadgets} this is an original list\n")
print (f"{sorted(gadgets)} aint an original list\n")# сделали сортировку, но не сохранили в переменную


#reverse (rotates the list on 180 degrees)

gadgets = ["telephone","Tesla","headphones","fridge","pip-boy"]
print (gadgets)
gadgets.reverse() #перевернули список 
print (f"{gadgets} this a reversed list\n")


#some additional tasks 

countries=["UK","New-Zeland","America","Russia","Italy"]
print (countries)
print (sorted(countries))
print (countries)
print(sorted(countries, reverse=True))
print (countries)
countries.reverse()
print (countries)
countries.reverse()
print (countries)
countries.sort()
print (countries)
countries.sort(reverse=True)
print (countries)

count=["1","2","3","4"]
count.append("5") #добавили элемент
count.insert(3,"10")
del count[1]
count.reverse()
count.sort()
count.pop()
count.remove("3")
print (count)


#for 

magic=["Love","Hate","Guns","Drugs"]
for mag in magic:
    print (mag)

for mag in magic:
    print (f"{mag.title()} nice ") #переменная mag идет в порядке возрастания в списке magic
    print (f"mb we can have some fun, what u think, {mag.title()}?")


print ("\nThats all for today folks !")


#range 

for value in range (1,5): 
    print (value) #будет печатать от 1 до 4 ( 5 не заденет, так как он увидел это значение и остановился)

print ("\nAnother example of usage 'range'")
for value in range (6):
    print (value) #выводит числа от 0 до 5

#making a list by using range

numbers = list (range(1,6))
print (numbers)


#making a list with steps by using range

numbers=list(range (2,11,2)) #ВАЖНО ---->> Список начинается со значения 2, а затем увеличивается на 2. Конец только в том случае, когда наше число будет или больше или равно 11 !!!!
print (numbers)


#List of squared numbers from 1 to 10

squares=[]
for value in range(1,11): 
    square=value**2 # ** - обозначает степент. 2**3 обозначает 2^3==8 
    squares.append(square)
    #OR YOU CAN DO IT THIS WAY
    #squares.append(value**2)
print (squares)


print ("\n min, max, sum")
# min, max, sum

numbers=list(range(-2,15,2))
x= min (numbers) #записываем в переменную x - минимум в списке
print (x) 

x= max (numbers) #нашли максимум
print (x)

x= sum(numbers) #сумма числового списка
print (x)


print ("\n list generator ")
# генератор списков

squares=[value**2 for value in range(1,11)]
print (squares) 

#Some tasks from the book

#1
for i in range (1,21):
    print (i)

#2
million=list(range(1,100_000_1))

#3
print (max(million))
print (min(million))
print (sum(million))

#4
spisok=list(range(1,21,2))
for i in spisok:
    print (i)

#5
spisok=list(range(3,31,3))
for i in spisok:
    print (i)

#6
spisok=[value**3 for value in range(1,11)]
print (spisok)


#working with the lists (slices)

players=["Michael","Lusiel","Mary","Comstock","Booker"]
print (players[0:3]) #выводит игроков от первого индекса до индекса, который мы указали -1
print (players[1:4]) 
print (players[:4]) # выводит всех игроков с самого начала списка до 4 индекса - 1
print (players[2:]) #выводит всех игроков со 2 индеса до конца
print (players[-3:]) #выводит всех игроков с самого начала до -3 индекса включительно ( что есть 2 индекс)

#brute force

print ("Here will be first 3 players\n")
for i in players[:3]:
    print (i)

#copying lists and some experiments with them

play=players[:] #так мы можем копировать списки
print ("\n")
print (play)

uno=["case","club","money"]
des=uno[:]
uno.insert(2,"love")
des.append("Haram")
print (uno,des)

fir=["uno","des"]
sec=fir #так мы показали, что sec=fir, что показывает питону, что любое изменение в одном из них, должно примениться и в других списках
fir.append("5")
sec.insert(0,"MAMA")
print ("First list",fir,"\nSecond list",sec)

#some additional tasks

lis=play[:]
print ("First three elements are", lis[:3])
lis.append("sup")
lis.append("dub")
lis.append("har")
lis.append("bar")
print (lis)
print ("Three elements in the middle are ", lis[3:6])
print ("Three elements in the end are", lis[6:])

pizza=["Margarita","Pepperoni","Diablo"]
fr_pizza=pizza[:]
pizza.append("Pineapple")
fr_pizza.append("lasagnia")
print ("\nMy pizza:")
for i in pizza:
    print (i)
print("\nFriend's pizza:")
for i in fr_pizza:
    print (i)


#Tuple

dimension=(100,500)
print (dimension[0],dimension[1])
dimens=(102000,) #Кортеж с одним элементом
print (dimens[0])

for i in dimension: #перебор
    print (i)

print ("non-modified tuple", dimension)
dimension=(500,1000)
print ("Modified tuple", dimension,"\n")

dimens=(100,200,300,400,500)
for i in dimens:
    print (i)


# if

lis=["junk","dank","horny"]
for i in lis:
    if i=="dank": #если переменная i будет равна dank, то в такое случае мы выводим 1 исход событий, в противном, 2 исход
        print (i.upper())
    else:
        print (i.title())

x="DANk"
if x.lower()=="dank":
    print("okay", x.lower())

#if + !=

x="Mom"
if x!="mom":
    print ("Nice")

#check two cases at one time (and)

age1=20
age2=25
age=15
if (age1>age) and (age2>age):
    print ("These both guys are olded than age")

#using or

age1=10
age2=15
age=13
if age1>age or age2>age:
    print ("well-well")


#checking if item in the list

lis=["hello","brolo","hi","bro"]
k="hi"
if k in lis:
    print ("He is in the list")

#check the lack of the item in the list

dis=lis[:]
k="bor"
if k not in dis:
    print("He is not in list")

#some tasks

li=[1,2,3,4]
bi=4
if bi in li:
    print (101)
if 5 not in li:
    print ("drake")

k="GORGe"
lis=["gorge","floyd"]
if k.lower() in lis:
    print ("Hell yeah")


#if else

age=17
if age==15: #проверяет переменную равна ли она 15 ( нет )
    print("Nice")
else: # если условие в if не выполняется, то питон переходит к else 
    print("change your value")

#if-elif-else

price=25
price1=40
age=int(input())
if age<=4:
    print ("free entrance")
elif age>4 and age<18:
    print("pay",price)
else:
    print("pay",price1)

#combos with elif

age=12 
if age>20:
    print("1")
elif age>15:
    print("2")
elif age>10:
    print("3")

#extra tasks

color="yellow" #Чтобы изменить исход, меняйте значение здесь
if color=="green":
    print("hey pal, you got 5 points\n")
else:
    print("Yo, you've just got 10 points!\n")

if color=="green":
    print("strike with the 5 points!")
elif color.title()=="Yellow":
    print("MMM, 10 points")
elif color=="red":
    print("you've got now 15 points, hell yeah")
else:
    print("thats loss")

age=int(input())

if age<2:
    print("baby")
elif age>=2 and age<4:
    print("Kinda child")
elif age>=4 and age <13:
    print("Teenager")
elif age >=13 and age<20:
    print("MMMM, AMATEUR")
elif age >=20 and age<65:
    print("an adult")
else:
    print("You live in russia, you should be dead right now")


#Using if with lists

requested_top=["mushrooms","green pepper","Chili peppers","onions"]
for request in requested_top:
    print (request, "Some adds")
print ("Your pizza is done")
for request in requested_top:
    if request!="green pepper":
        print("Making your pizza...")
    else:
        print ("Oh shit i am sorry, your pizza will have a lack of a pack with green peppers")

requested_topp=[] # список пуст, поэтому if не будет выполняться (ибо он смотрит, есть ли что-нибудь в списке)
if requested_topp:
    for request in requested_topp:
        print("mmm, nice ingredient, m'am", request)
    print ("Well, your pizza is ready to be consumed!\n")
else:
    print("Strange, but your pizza is plain. You sure you want that one ?\n")

#Multiple lists

available_topping=["Mushrooms","Ketchup","Onions","lasagna"]
requested_topp=["Bikmakbetov","mushrooms","onions"]
for request in requested_topp:
    if request.title() in available_topping:
        print (f"Adding some {request}")
    else:
        print ("sorry, we dont have", request)

#Additional tasks
##1 
users=["Jake","Robert","Falcon","admin"]
if users:
    for user in users:
        if user.title()=="Admin":
            print("welcome home, king")
        else:
            print (f"Hey, {user}")

##2
users=[]
if users:
    print("hello world")
else:
    print("No users :(")

##3
us1=["Jake","Harold","Mick","Angie","Barnie"]
us2=["holt","Kolt","mick","jake"]
for user in us2:
    if user.title() in us1 or user.lower() in us1 or user.upper() in us1:
        print (f"Sorry ,but {user} is already taken by the other person")
    else:
        print("Proceeding...")

##4
ls1=[1,2,3]
ls2=[1,2,3,4,5,6,7,8,9]
for i in ls2:
    if i in ls1:
        if i==ls1[0]:
            print (f"{i}st")
        elif i==ls1[1]:
            print (f"{i}nd")
        else:
            print(f"{i}rd")
    else:
        print (f"{i}th")


...



