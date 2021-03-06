#import this # delete the first hashtag to see the truth


#String methods 

#isAlpha возвращает True, если строка состоит только из букв и не является пустой
print ('hello'.isalpha())
print ('hello1'.isalpha())

#isalnum возвращает True , если строка состоит из букв и цифр
print ('hello12'.isalnum()) 
print ('hello'.isalnum()) 

#isdecimal возвращает True , если строка состоит только из цифровых символов и не является пустой
print ('123'.isdecimal())
print ('hello'.isdecimal())

#isspace возвращает значение True если строка состоит из символа пробела, табуляции , новой строки и не является пустой
print (' '.isspace())
print ('hello '.isspace())

#istitle Возвращает True , если все слова начинаются с большой буквы , а потом с маленькой 
print ('Hello World'.istitle())
print ('Hello WORLD'.istitle())

#startswith and endswith - первый метод направлен на проверку, начинается ли строка с символа(или слова), который написан в скобках. Второй метод проверяет последнее слово
print ('hello mama'.startswith('hello'))
print ('hello mama'.endswith('mama'))

#join and split - Первый метод соединяет все слова с списке с помощью символа, который мы прописываем в начале. Второй метод - разделяет предложение (aka string) , на объекты в списке. 
print (', '.join(['cats','dogs','lions'])
print ('my name is human'.split())
# если мы хотим разделить все это по определенному принципу, то надо прописать в split , по какому именно
print ('myABCnameABCisABChuman'.split('ABC'))

#center и rjust , ljust
print (('hello').center(20,'=') #Такой метод будет полезен, если мы хотим создать более-менее адекватный юзер интерфейс

       
#deleting and inserting different stuff in list

baba = ["mama","papa","babu"]
message = f"my first kiss was with\n\t{baba[1].title()}" # f перед ковычками дает нам возможность писать переменные в str формате, но только в спец скобочках {}
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


#Alphabet

alien_0={"colour" : "green" , "points" : 5} #Словарь состоит из Ключа и значения. Ключ это то, что стоит слева от ":" а значение это то, что стоит справа. Ключ - значение может быть бесконечное кол-во в словаре, так что пользуйтесь им, если есть возможность 
print (alien_0["colour"]) #Чтобы обратиться к значению в ключе, надо прописать его ключ, что мы и сделали сейчас
print (alien_0["points"]) #Тут мы прописали ключ от "очков" и увидели значение 5

new_points=alien_0["points"]
print ("You've just earned", new_points,"points")

#Adding new pairs in the Alphabet

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print (alien_0)

#Making an empty alphabet

alien_0={}
alien_0["Colour"]="Blue"
alien_0["points"]=10
print (alien_0)

#Change the variable in the alphabet

alien_0 = {"colour": "green"}
print (alien_0["colour"])
alien_0["colour"]= "Yellow" #Таким простым способом, мы изменили у ключа colour значение с green на Yellow
print (alien_0["colour"])

alien_0={"x_position" : 0,"y_position": 25,"speed": "medium"}
print (f"Position of the alien is {alien_0['x_position']} ")
print ("An alien is moving rightwards")
print ("Counting the size of the move to get that piece of shit")
if alien_0["speed"]=="slow":
    x_increment=1
elif alien_0["speed"]=="medium":
    x_increment=2
else:
    print("He is so fast, my god")
    x_increment=3
alien_0["x_position"]=alien_0["x_position"]+x_increment
print (alien_0["x_position"])

#Deleting key-variable

alien_0={"colour":"green","points":20}
print (alien_0)
del alien_0["points"]
print (alien_0)

#An alphabet with the same objects

favourite_language={
    "jen":"python",
    "sarah":"c",
    "edward":"ruby",
    "phill":"python"
}
print (favourite_language)
language=favourite_language["sarah"].title()
print (favourite_language)
print (language)

#GET

alien_0={'colour':"green","speed":"slow"}
point=alien_0.get("points","No point assigned")
print (point)
print (alien_0.get("Point"))

#More tasks to do!
##1
person={"First name": "David", "Second name":"Bowie","City":"Lodnon","Year": "1962"}
for i in person:
    print (person[i])

##2
person={"Andrew": "1", "Hopki" : "5", "Jorge" : "21", "Lara" : 69, "Lony" : 999, "Donki" : "baba", "Karla" : 999}
for i in person:
    print (i, person[i])

#Brute through the Dictionary

for key,value in person.items(): #Метод items нужен для вызова связки key - value. В key будут идти значения из ключа , а в value из значения ( key , value могут быть переименованны, как захотите)
    print (key)
    print (value,"\n")

#Brute all keys in the Dictionary 

for i in person.keys(): #метод keys используется для присваивания i (или любой другой вашей переменной) значение ключа 
    print (i)

friends=["Donki","Andrew"]
for i in friends:
    if i in person:
        print (i,"ain't here and his favourite", person[i].title())
    else:
        print (i,"Is here ")


print ("\nJust making some space...\n")
#Brute keys in special queue

for name in sorted(person.keys()):
    print (name)

#Brute all values in the dictionary

for i in person.values(): #Метод value работает также, как и keys, только вместо ключей, он выводит значения
    print (i)

print ("\nJust making some space...\n")


for i in set(person.values()):
    print (i)

words={"Love" : "Chemistry", "Health" : "Lack of something", "Will": "Something why we still live"}
words["Bank"]="Robery"
for i,k in sorted(words.items()):
    print (f"I've got {i.title()} and {k.upper()}")

#Lists of dictionnaires

alien_0={"colour" : "green", "points" : 5}
alien_1={"colour" : "yellow", "points" : 10}
alien_2={"colour" : "red", "points" : 15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print (alien)

print("\nJust making some space...\n")

aliens=[]
for alien in range (30):
    alien={"colour":"green","points":5}
    aliens.append(alien)
print (aliens[5:10])
print (len(aliens))

print("\nJust making some space...\n")

for alien in aliens[2:5:2]:
    if alien["colour"]=="green":
        alien["colour"]="Yellow"
        alien["speed"]="Medium"
        alien["points"]=10


for alien in aliens[0:10]:
    if alien["colour"]=="green":
        alien["colour"]="Yellow"
        alien["speed"]="Medium"
        alien["points"]=10
    elif alien["colour"]=="Yellow":
        alien["colour"]="Red"
        alien["speed"]="High"
        alien["points"]=15
print (aliens[0:10])

#lists in dictionnaires

pizza={"Wheat": "Natural", "Sauce":"mayonnaise", "toppings" : ["onions","garlic","potato"]}
for i,k in pizza.items():
    if type(k)==str:
        print (f"Adding {i} ")
    else:
        for j in k:
            print (f"And your favourite toppings {j} are coming")

#Dictionary in the Dictionary 

users={
    "aeinstein":{
        "first":"Albert",
        "last":"einstein",
        "city":"princetion"
    },
    "marie":{
        "first":"Mary",
        "last":"Poppins",
        "city":"London"
    },
}
for user,name in users.items():
    print (user.title())
    print (f"\tfull name {name['first']} {name['last']}")
    print (f"\tcity {name['city'].upper()}")

#Additional tasks
#1
person_0={"Name":"David","Surname":"Bowie","City":"London"}
person_1={"Name":"Norman","Surname":"Reedus","City":"USA"}
person_2={"Name":"Evgeni","Surname":"Grinko","City":"Moscow"}
person=[person_0,person_1,person_2]
for per in person:
    for i,k in per.items():
        print (i.upper(),k)
    print("\n")

#2
places={"Evgeni":["Moscow","Austria","Germany"], "Dan":["Denmark","Italy"]}
for i,k in places.items():
    print(i.title(),"wants to visit")
    for j in k:
        print ("\t",j)

#3
cities={"Moscow":{
    "population":"1000000",
    "jobs":"Available",
    "nature":"Dead"
    },
    "Afganistan":
    {
        "population":"-1",
        "jobs":"soldiers",
        "nature":"Alive AF"
    },
    "USA":
    {
        "population":"1000000000000",
        "jobs":"OILY JOBS ONLY",
        "nature":"Kinda alive"
    }
}
for i,k in sorted(cities.items()): #i - Moscow\USA\Afganistan . k - информация которая хранится в словарях (значение)
    print (i.upper())
    for j in k: #j у нас выступает в качестве ключа в самом словаре (population,jobs,nature)
        print (f"Here is stat about this country {j.title()} - {k[j]} ")#Именно поэтому мы и используем словарь k 


#WHILE
#input

message=input("Tell me something sweet: ")# внутри input можно вписать все, что хочешь и пользователь это увидит, когда будет вводить значения
print ("nice",message,"\n")

promp="hey"
promp+="\tnice coding skills\n" #Можно таким образом соединить 2 сообщения в одно
message=input(promp) #а здесь , вместо текста, можно вывести наше сообщение, которые мы до этого писали
print ("AE", message)

#using int in input

age=input("How old are you? ") #даже вводя число, питон все равно видит его, как str (буквенно значение)
print (age)
print (type(age))

print ("\nMaking some space\n")

age=input("How old are you?\nVersion N2 ")
age=int(age) #Если мы ввели число, то в этом случае мы переводим его из str в int (из букв в цифры)
print (age>18) 
           
# calculating residue by using % operator

print (4%3) #4-3=1 (остаток 1)
print (5%3) # 5 - 3 = 2 ( вычисляем остаток)
print (6/3) # 6 -3 -3 (идет простое деление на 2)

x=int(input("Введите число, которое вы хотите проверить на четность\n")) #ввели число (поставив int перед вводом, чтобы не пришлось расписывать это действие в 2 строках)
if x%2==0: #проверили, делится ли число, которое мы ввели на 2 без остатка 
    print ("Четное")
else:
    print ("Нечет")

#Extra tasks
#1
x=input("Your favourite car\n")
print (f"I like your {x}")

#2
x=int(input("Введите сколько столов вам нужно\n"))
if x>8:
    print ("Надо будет подождать")
else:
    print ("Ждите, скоро все будет готово")

#3
x=int(input("Введите число, которое вы хотите проверить на кратность 10\n"))
if x%10==0:
    print ("Оно кратно 10")
else:
    print ("Некратно")

#Cycles with While

number=1
while number <=5:
    print (number)
    number+=1

#users chooses when to stop the programm

words="\tTell me anything you want and i will repeat it to u"
words+="\t\notherwise ,if you type 'quit' i will stop myself "
message=""
while message !="quit":
    message=str(input("Enter your words\t"))
    if message !="quit":
        print (message)

#flags

flag=True
while flag: #Весь while работает по принципу -> пока правда - делаю. В данном случае flag мы изначально указали , как правда (True), поэтому цикл и выполняется
    x=str(input("Введите сообщение и я вам его напишу\nЕсли захотите завершить программу, напишите 'quit' "))
    if x!="quit": #спрашиваем питон, чему равен x , если все что-угодно, кроме quit, то тогда мы продолжаем программу
        print (x)
    else:
        flag=False #в данном случае наш flag стал равен False  - ложь и поэтому while заканчивает свою программу

#break in while

message="Введите слово и я его повторю"
message+="\n\tВ противном случае, введите 'quit' и программа остановится "

while True :
    mes=input(message)
    if mes=="quit":
        break #break останавливает while (даже если тот находился в бесконечной рекурсии). ВНИМАНИЕ break хоть и полезен, но он влечет за собой большее время выполнения программы
    else:
        print (mes.title())

#continue in while

number=0
while number <=10:
    if number%2==0:
        number+=1
        continue #continue продолжает код ( без прерываний)
    else:
        print (number)
        number+=1

#Avoiding infinite cycles 

x=1
while x<=5:
    print (x) # в этом случае , будет бесконечный вывод единиц. Чтобы ,в таком случае, завершить программу , потребуется нажать или cntrl+c (Win) или command+c(IOS\APPLE)
    
#Extra tasks
#1

message="Вводите топпинги, которые вы хотите добавить в пиццу"
message+="\nЕсли захотите завершить заказ топпингов - напишите 'quit'\n"
flag=True
while flag:
    x=input(message)
    if x!='quit':
        print (f"добавляем {x} в вашу пиццу\n")
    else :
        flag=False

#2

while True:
    x=int(input('Введите ваш возраст\n'))
    if x<3:
        print ("Поздравляем, ваш билет бесплатный\n")
    elif x>=3 and x<12:
        print ("Стоимость билета 10 руб\n")
    else:
        print ("Стоимость билета 15 руб\n")
    break

#3

flag=True 
while True and flag:
    x=input("Введите топпинг для пиццы. Если захотите завершить программа - напишите quit ")
    if x!='quit':
        print (f"добавляем {x}")
    else:
        flag=False
        break

#Using while with lists and dictionaries
#Moving elements between lists

uncomfirmed_users=["lara","colin","dave","Gorge","kate"]
confirmed_users=[]
while uncomfirmed_users:
    user=uncomfirmed_users.pop()
    print (f"varification is coming for {user.upper()} ")
    confirmed_users.append(user)
print (confirmed_users)
print ("an old list", uncomfirmed_users)

#delete all elements from this list with the stated variable

pets=["cats","dogs","penguin","parrot","elephant","Cats"]
while "cats" in pets or "Cats" in pets: #Пока одно значение в списке или другое значене в списке -> выполнять действие
    if "cats" in pets:
        pets.remove("cats")
    else:
        pets.remove("Cats")
print (pets)

#Filling the dictionary with user's data (using while)

responses = {}
active=True
while active:
    name=str(input("Please enter your name\n"))
    respons=input("Which mountain have ever wished to climb on\n")
    responses[name]=respons

    repeat = input("Would you like to continue the process ? (type 'no', to stop)\n")
    if repeat=="no":
        active=False
for i,k in responses.items():
    print (f"\n{i} really would like to climb {k}\n")

#Extra tasks
#1 and 2
sandwich_orders=["pastrami","ham and cheese","pastrami","pastrami","Tuna","pastrami","beaver sandwhich","pastrami","Kadgit's sandwhcih"]
finished_sandwiches=[]
while sandwich_orders:
    if "pastrami" in sandwich_orders:
        while "pastrami" in sandwich_orders:
            sandwich_orders.remove("pastrami")
    finished_sandwiches.append(sandwich_orders.pop())
for i in finished_sandwiches:
    print (f"we've done this sandwhich {i}")

#3

respons={}
while True:
    x=input("Hello, please enter your name\n")
    y=input(f"thanks {x}, now please enter a place where you want to chill out\n")
    respons[x]=y
    x=input("lets continue. If you want to stop, please enter '-' or 'no'\n")
    if x=="no" or x=="-":
        break

for i,k in respons.items():
    print (f"\n{i} wants to go to {k}")


#FUNCTIONS
#ФУНКЦИИ ! Для чего они же нужны ? Ну... К примеру, если вам требуется выполнить какой-то определенный блок кода неск раз. Разумеется, можно использовать различные циклы и не только, но использование функций ведет за собой ускорение работы программы + код с функцией проще отлаживать, да и вообще проще читать, что влечет за собой уйму плюсов. Функции используются всеми и везде. Скоро вы сами в этом убедитесь

def greet (): #после def (это так называемый "идентификатор" для питона, который показывает, что МЫ СЕЙЧАС БУДЕМ ПИСАТЬ ФУНКЦИЮ) после def идет название нашей функции (можете назвать как хотите), но не надо называть функции, которые начинаются и заканчиваются на это __ (пример того, что не стоит писать ,пока не разберешься -> __init__ <- это название для функции служит для того, чтобы каждый раз при включении программы эта функция выполнялась (внутри самой функции можете писать что хотите))
    print ("Hello there")
    print ("Hello , General Kenoby")

greet()
"""В данном случае мы написали программу, которая решает лишь одну задачу. Написать пару реплик из звездных войн :)\nпозже я вам покажу, как функции могут в игры и вообще в разный тип простых/сложных задач """
#когда вы хотите что-то задокументировать, просто используйте тройные кавычки """ЧТО-ТО НАПИСАЛИ""" вот и все (в противном случае, можете продолжать использовать хэштэги (#))0))0

#Translating information to the function

def greet_user (username): #если мы хотим что-то включить в функцию, мы должны прописать это в в круглых скобочках
    print ("Hello there")
    print (f"Hello ,general {username.upper()}")

greet_user("monkey") #а вот здесь мы пишем, что именно мы хотим юзануть
greet_user("D.VA")

#virables and paramets

#def greet_user (USERNAME) что же такое username ? Это параметр, который может быть изменен, как вы захотите 
#greet_user("monkey") в данном случае monkey (или D.VA) является аргументом, который мы передаем в функцию (или же в параметр в функции) после чего username сохраняет monkey в себе. Проще говоря, username(или что-то другое (все зависит от того, как вы это назовете)) это типа такая переменная, в которую можно передать любое говно, которое вы напишите при вызове функции. После этого переменная username может служить вам для разных целей НО ТОЛЬКО В ПРЕДЕЛАХ ФУНКЦИИ (Первое правильно функции: все что происходит в функции - остается в функции). Останутся вопросы - пишите мне в вк(ссылка на него есть в профиле)


#extra tasks
#1
def display_message():
    print ("Hello guys, our today's theme is functions in python")

#2
def favourite_book(YaEbal):
    print (f"One of my favourite books is {YaEbal}")

favourite_book("Alice in the wonderland")

#positional arguments

def describe_pet(animal_type, pet_name): #в функции ( и в вызове функции ) мы можем спокойно перечислять элементы (коих может быть беск число)
    print (f"Тип животного {animal_type.title()}")
    print (f"Имя сего существа {pet_name}")

describe_pet("hamster","DOGE")
describe_pet("Barbie","Doll")

#named arguments

def described_pet(animal_type, pet_name):
    print (f"Тип животного {animal_type.title()}")
    print (f"Имя сего существа {pet_name}")

described_pet(animal_type="Villain", pet_name="Joker") #Если перед каждым аргументом мы будет писать, что это за тип переменной, то питон без проблем будет все юзать ( да и не будет лишней возни)
described_pet(pet_name="Harley Davidson", animal_type="Bike") #в таких вызовах легко можно зафакапить все, потому что надо правильно написать имена параметров в функции, иначе будет ошибка

#Default argument

#В функции параметру можно присвоить значение по умолчанию. Если мы передаем в него что-то ,то значение опустится (чтобы лучшее это понять, смотрите код ниже)

def my_pet (pet_name, pet_type="Doge"):
    print (f"My pet's name is {pet_name.title()}")
    print (f"{pet_name}'s type is {pet_type}")

my_pet("willie") #тут не пишем 2 значение, потому что у нас есть уже значение по умолчанию
my_pet("Gary","cat") #тут мы пишем, потому что у нас кошка
my_pet ("larry") # тут мы опять не пишем, потому что у нас собака

#Extra tasks
#1
def make_shirt (size=0,text="No print"):
    print (f"The size of the T-shirt is {size} and the text on it will be - {text}")

make_shirt(40,"hi")
make_shirt(10,69)
make_shirt(10)

#2

def describe_city (town="LA",country="the USA"):
    print (f"{town} is in {country} !")

describe_city("Moscow","Russia")
describe_city()

#returning an object from the function

def form_name (first_name=None,last_name=None):
    full_name=f"{first_name} {last_name}"
    return (full_name.title()) #return тут работает, как способ, чтобы передать переменную из функции в переменную в основном коде (в данном случае это x)

x=form_name("jack","nickolson") #Чтобы return сработал, как надо, требуется , чтобы переменная обозначала вызов функции (как здесь). return возвращает, что нам надо из функции в переменную x, которую мы потом и используем 
print (x)

#optional arguments

def formatted_name (first_name=None,last_name=None, middle_name=""): #необязательные аргументы нужны для того, чтобы в некоторых случая мы могли просто опустить некоторы данные ( как в нашем случае). Делается это точно также, как и при присваивании значения по умолчанию, только тут вместо текста стоит просто пространство (попробуйте сами, это рил просто)
    full_name=f"{first_name} {middle_name} {last_name}"
    return full_name.title()

homie=formatted_name(first_name="John",last_name="lee",middle_name="Hooker")
print (homie)
homie=formatted_name("John","Mordovich")
print(homie)

#returning of the dictionary 

def build_person(first_name=None,last_name=None, age=None):
    person={"first":first_name.title(),"second":last_name.lower()}
    if age:
        person['age']=age
    return (person)

guy=build_person("jack","NICOLSON", age=69)
for i,k in guy.items():
    print (i,k)

#using functions in while

def frr_name (first_name=None,second_name=None):
    full_name=f"{first_name} {second_name}"
    print (f"Hello {full_name}")
    return full_name.title()

while True:
    print ("Please tell me ur name m8\n")
    x=input("Name: ")
    y=input("Aaaand your surname: ")
    name=frr_name(x,y)
    print (name)
    x=input("if you want to stop, please type 'no'\n")
    if x=="no":
        break

#Extra tasks
#1
world={}
def city_country(city,country,world):
    world[country]=city
    return world

for i in range(3):
    x=input("Enter your country: ")
    y=input("Enter your city: ")
    city_country(y,x,world)
print (world)

#2

def make_album(name,producer,album,nub=None):
    alb={}
    alb["name: "]=name
    alb["producer: "]=producer
    alb["Album's name: "]=album
    if nub:
        alb["number of tracks: "]=nub
    return (alb)

first_album=make_album("David Bowie","David Bowie","Blackstar",9)
second_album=make_album("Corey Taylor","Stone sour","death")
print (first_album)
print (second_album)

#transporting list

def greet_users(names):
    for i in names:
        msg=f"Hello {i}"
        print (msg)

users=["hannag","Keil","Jake","Bro"]
greet_users(users)

#change list in the function

unprinted=["phone","Xbox","Playstation","PC"]
printed=[]
while unprinted:
    current=unprinted.pop()
    print (f"current design {current}")
    printed.append(current)

for i in printed:
    print (i)

"""OR WE CAN DO THIS WAY"""

def print_models(unprinted,completed):
    while unprinted:
        current=unprinted.pop()
        print (f"{current} is in progress")
        completed.append(current)

def show_models(completed):
    for i in completed:
        print (i)


unprinted=["phone","Xbox","Playstation","PC"]
completed=[]
print_models(unprinted,completed)
show_models(completed)

#restriction of changing list in function

def print_models(unprinted,completed):
    while unprinted:
        current=unprinted.pop()
        print (f"{current} is in progress")
        completed.append(current)

def show_models(completed):
    for i in completed:
        print (i)


unprinted=["phone","Xbox","Playstation","PC"]
completed=['hi']
print_models(unprinted[:],completed)
show_models(completed)
print ("showing the copied list")
show_models(unprinted)

#Extra tasks
#1
mes=["hi","thank you","you welcome"]
show_models(mes)

#2

def send_message(sending,sent):
    while sending:
        msg=sending.pop()
        print (msg)
        sent.append(msg)

mes=["hi","thank you","you welcome"]
sent=[]
send_message(mes,sent)
print ("messages that didnt get to the point")
show_models(mes)
print ("Messages which reached the point")
show_models(sent)
send_message(mes[:],sent) 
print ("messages that didnt get to the point_1")
show_models(mes)
print ("Messages which reached the point_1")
show_models(sent)

#transfering custom variables

def make_pizza(*toppings): # * в данном случае создает кортеж в который можно запихнуть скок хош значений
    print (toppings)

def made_pizza(*toppings): #теперь наша функция выводит не весь кортеж разом , а все элементы один за другим
    for i in toppings:
        print (i)

make_pizza('pep')
make_pizza("mushrooms","green peppers","extra cheese")
made_pizza('pep')
made_pizza("mushrooms","green peppers","extra cheese")

#positional arguments with custom sets of aruments (damn that sounds hard)

def mad_pizza(size,*toppings): #если вы заранее знаете , что у вас будет много разной инфы , которую можно запихнуть куда-угодно, то после определения нужных вам параметров, используйте *переменная. Чтобы лучше понять - смотрите код
    print (size) #И да, лучше использовать определенное имя переменной *args  - вот так, чтобы все точно понимали, что в эту переменную вы будете пихать много значений и не только
    for i in toppings:
        print ("-",i)

mad_pizza(69,"mushrooms")
mad_pizza(420,"mushrooms","green peppers","extra pepper","onions") 

#using custom number of arguments 

def build (first,last,**user_info): #** звездочки создают уже не кортеж, а словарь,в который можно добавлять бесконечное кол-во ключ-значений, что может быть очень полезно при написании парсера или прочих других массивов и баз данных
    user_info['first_name']=first
    user_info['last name']=last
    return (user_info)

user_profile=build("albert","einstein",location='princerton',field="physics")
print (user_profile)

#extra tasks
#1
def sandwhich (type_of_bread,mains,type_of_cheese,*extras):
    print (f"Oki-doki, your type of bread will be {type_of_bread} and ur main ingridients will be {mains}. Type of cheese is {type_of_cheese} and your extras: ")
    for i in extras:
        print (i)
    print ("\n")

sandwhich("wheat","Cucumbers and meat","Funky one", "onions", "mushrooms")
sandwhich("wheat","Cucumbers and meat","Funky one", "onions")
sandwhich("wheat","Cucumbers and meat","Funky one", "onions","pepper souce", "mushrooms","extra milk")

#2

def build_task (first,last,**user):
    user['first_name']=first.title()
    user['last name']=last.title()
    return (user)
uno=build_task("mark","kronbergs",job="programmer",children="None",games="WOW")
des=build_task("Dan","parsovich",meaning="There is no meaning of my life",love="there is no love",addictive_to="gaming",mental_issues="got them")
print (uno)
print (des)

#3

def automobile(maker,name_of_the_model,**extra_info):
    extra_info["maker"]=maker.title()
    extra_info["Name of the model"]=name_of_the_model.title()
    return (extra_info)

x=automobile("x5","subaru",colour="blue",amount=5,quality="Good")
y=automobile("is","whore",you="your",mam="mama")
print (x)
print (y)

#storing functions in modules
#importing the whole module
#Импортирование ! Для чего же оно нужно и как все работает ? У вас есть функции и вы не хотите засорять код ? Тогда ответ прост ! Создайте какой-нибудь файл.py в том же каталоге(папке), что и ваш основной файл и спокойно пишите imoprt название вашего файла

#Line 4 (imports file)
import ports

ports.make_pizza(16,"pepperoni") #После того, как вы сделали импорт файла , используйте название файла.название функции и пишите код так, будто бы функция сейчас находится в вашем основном коде !
ports.make_pizza(69,420,"few cucumbers")

#imoprt chosen functions
#если не хотите импортировать ВЕСЬ , то можно заюзать метод, который будет описан ниже

from ports import make_pizza #после применения этого порта, вы можете спокойно использовать функции, которые находятся в нем
make_pizza(69,420,"few cucumbers")
make_pizza(20,"calculate","Karamba")

#making a pseudonym for a function

from ports import make_pizza as mp #Из файла ports мы импортируем функции make_pizza под именем mp(название основной функции не меняется)
mp(6,42,"few cucumbers ?")
mp(20,"calculate 1111","Karamba")

#making a pseudonym for the module 

import ports as por
por.make_pizza(70,20,"few cucumbers")
por.make_pizza(21,"calculate","Karamba")

#import all the stuff

from ports import * #* в данном случае обозначает импортировать из этого файла ВСЁ. Хоть эта функция довольно-таки крута, но она может повлечь за собой очень негативные последствия (к примеру: в основном коде есть уже функция с похожим названием. Такой импорт повлечет за собой замену функции в основном коде на ту, которая импортировалась)
make_pizza(70000,21212310,"a few cucumbers")
make_pizza(1010201201,"KArak","Karamba")

#Extra tasks
#1

#Line 11 (imports.py)
from ports import *

unprinted=["phone","Xbox","Playstation","PC"]
completed=[]
print_models(unprinted,completed)
show_models(completed)

#2

import ports
from ports import print_models
from ports import print_models as pm
import ports as PR
from ports import *


#CLASSES 
#КЛАССЫ 
#Классы позволяют делать много разных вещей, к примеру , возьмем МОБов (или НПС) из видеоигр. Рассматривать мы будем Minecraft и житилей деревни. Как известно, в деревне есть жители (считай, это общий класс). У каждого жителя есть свои задачи и назначения, к примеру , есть простой житель, который гуляет по городу (это уже объект (или же функция def )). Получается, есть продавец, есть фермер и тд, и у каждого из них есть своя роль, но так как у многих жителей есть повторяющиеся роли, мы просто берем и юзаем функцию, чтобы назначить жителю роль. В итоге, если все максимально упростить, класс - это деревня (или же список со всеми ролями), а объекты - это роли, которые могут повторяться и которые можно изменять ( если залезть в сам класс) 

class dog(): # Определяем новый класс (если создаем новый класс, то в скобках ничего не пишем)

    def __init__(self, name, age): # метод __init__ (и прочие другие , но о них потом) уникален. Когда он находятся в классе, то при каждом вызове экземпляра (функции), автоматом выполняется этот экземпляр 
        #Инициализация атрибутов name и age 
        self.name=name # self нам , в данном случае, нужен для того, чтобы переменная была доступна во всем классе (в других функциях вы можете заметить, что там мы это уже не прописываем, потому что self дает нам возможность это не делать )
        self.age=age
    
    def sit (self): #self - что же это ? во-первых, метод self, всегда должен стоять на первом месте, когда мы пишем функцию (сейчас вы видите это в коде) и self нужен, чтобы питон кидал в него ссылку на экземпляр ака доступ к атрибутам и методам класса
        print (f"{self.name} cел ")
    
    def roll_over (self): #Короче говоря, всякий раз , когда будете юзать класс и функцию в нем , не забывайте писать в самой функции ( в списках аргументов) self на первом месте
        print (f"{self.age} вот это возраст ! Удивительно, как он может вообще перекатываться")

my_dog=dog('willie',6) #чтобы использовать класс, мы сначала должны приказать питону создать экземпляр с кличкой willie и возрастом 6. Уже во время обработки этой строчки, вызывается метод __init__
print(f"My dog's name is {my_dog.name}")
print (f"My dog is {my_dog.age} years old")

#"talking with atributes"

print (my_dog.name) # Этот тип записи называется "точечная запись" и такая запись поможет нам взять значения атрибутов из класса на последний момент

#using method

my_dog.sit()
my_dog.roll_over()

#making a few specimen

my_dog=dog("Naggets",5)
your_dog=dog("Bangladesh", 11)

print (f"{my_dog.name} can't do a lot as {your_dog.name} ")
print (f"funny, but my dog is {my_dog.age} years old and yours is {your_dog.age} old")

#Extra tasks
#1

class Restaurant():

    def __init__ (self,name,cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
    
    def desctibe (self):
        print (self.name)
        print (self.cuisine_type)
    
    def open_restaurant(self):
        print ("Restaurant is open now")
    
restaurant=Restaurant("Uzbechkina","Uzbekistan food")
print (restaurant.name)
print (restaurant.cuisine_type)
restaurant.desctibe()
restaurant.open_restaurant()

#2

restaurant1=Restaurant("Kalmik","Kazakh's famous food")
restaurant2=Restaurant("Arab tut bil","Arabic food")
restaurant1.desctibe()
restaurant1.open_restaurant()

restaurant2.desctibe()
restaurant2.open_restaurant()

#3

class User:

    def __init__(self):
        print("\nhello , admin\n")

    def first_name(self,name):
        self.name=name
    
    def last_name(self,l_name):
        self.l_name=l_name
    
    def info (self,*args):
        self.args=args
    
    def describe_user(self):
        print (f"Hello {self.name} {self.l_name} i know so much about you, for example: ")
        for i in self.args:
            print(i)
    

    
user=User()
user.first_name("Arkovich")
user.last_name("Mordovich")
user.info("Loves gaming","fan of night clubs","Cigarettes addictive")
user.describe_user()

#working with classes and speicmen

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


my_car=Car('audi','a4',2019)
print (my_car.desryption())
my_car.read_metr()

#changing atributes in class 
#1 method

my_car.odometr=23
my_car.read_metr()

#2 method

my_car.update_odom(20)
my_car.read_metr()
my_car.update_odom(-1)
my_car.read_metr()

#3 method

my_used=Car('subaru','outbreak',2015)
print (my_used.desryption())

my_used.update_odom(23_500)
my_used.read_metr()

my_used.increasement(1000)
my_used.read_metr()

#extra Tasks
#1

class Restaurant_1():

    def __init__ (self,name,cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
        self.number_served=0
    
    def desctibe (self):
        print (self.name)
        print (self.cuisine_type)
        print(self.number_served, "people served")
    
    def open_restaurant(self):
        print ("Restaurant is open now")
    
    def update_people(self,num):
        if num>0:
            self.number_served+=num
        else:
            print ("It is illegal !")
    def set_peope(self,num):
        self.number_served=num

rest=Restaurant_1("ching-chong","chinese food")
rest.set_peope(4)
rest.desctibe()
rest.update_people(-1)
rest.update_people(10)
rest.desctibe()

#2

class User_1:

    def __init__(self,num):
        self.num=num
        print("\nhello , admin\n")

    def first_name(self,name):
        self.name=name
    
    def last_name(self,l_name):
        self.l_name=l_name
    
    def info (self,*args):
        self.args=args
    
    def describe_user(self):
        print (f"Hello {self.name} {self.l_name} i know so much about you, for example: ")
        for i in self.args:
            print(i)
        print ("Number of your attempts is", self.num)
    
    def login_increase(self,num):
        if self.num>num:
            print ("this is forbidden")
        else:
            self.num=num
        
us=User_1(0)
us.first_name("Leo")
us.last_name("Caprio")
us.info("Loves football","filming is his passion")
us.describe_user()
us.login_increase(1)
us.describe_user()

#inheritance
#Method __init__ for the class inheritance

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

class Electric_car(Car): 
    #сейчас мы создаем потомка основного класса. Потомок является классом-потомком родителя, что значит, что он обладает теми же свойстами, что и родитель, только у него есть дополнения. К примеру, возьмем машину (класс - родитель) и электромашину (класс-потомок) и дизельную машину (еще один потомок). У всех этим машин есть что-то общее - 4 колеса , стекла , руль и тд, но чем-то они отличаются и именно для этого и создаются потомки, чтобы не было лишней путаницы и проблем в классе родителе. Так, в потомке электромашин мы указали топливо - электричество , а в другом потомке - топило дизель

    def __init__(self,make,model,year):
        super().__init__(make,model,year)# супер позволяте вызвать метод род класса. Она приказывает метод init класса Car 
        self.battery=75
    
    def describe_bat(self):
        print (f"This car's got {self.battery} KWH left")
    
    def fill_gas_tank(self,nub):
        print ("This type of car doesn't need it !")


my_tesla=Electric_car('tesla','models s','2019')
print (my_tesla.desryption())
my_tesla.fill_gas_tank(5)

#giving atributes and methods of parent class
my_tesla.describe_bat() 

#changing methods of the parent class
    # def fill_gas_tank(self): Этот метод добавляется в класс Elcetrocar и нужен он для того, чтобы не было таких проблем , как !. Предположим кто-то решил вызвать метод заправки топливом для машины (в классе Car) и тут все нормально и проблем нет, но если кто-то возьмет класс электрокар и попробует заполнить его бак, то это может вызвать конфуз для чего мы прописали метод ( С ТЕМ ЖЕ ИМЕНЕМ, что и в родителе ) в классе-потомке Электромобиль
    #     print ("This type of car doesn't need it !") 

#example as an atribute

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

my_tesla=Electric_car('tesla','models s','2019')
my_tesla.battery.describe_battery() #Что же тут происходит ? Тут можно элементарно запутаться, поэтому будем двигаться аккуратно . Сначала мы сделали переменную my_tesla с фишечками род класса ( и его подкласса), после этого мы взяли атрибут battery (типа self.batter это как наша переменная. Вызов похож, как если бы мы создавали переменную my_tesla) и взяв этот атрибут мы сказали, какую функцию мы хотим выполнить и всё !
my_tesla.battery.get_range() 

#Extra tasks
#1

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
    
restaurant=Restaurant("Uzbechkina","Uzbekistan food")
print (restaurant.name)
print (restaurant.cuisine_type)
restaurant.desctibe()
restaurant.ice_cream_stand()
restaurant.open_restaurant()

#2

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
    # def privileges (self, add="Can add users",forbidden="can deleate users" ,ban="can ban users"):
    #     self.forbidden=forbidden
    #     self.add=add
    #     self.ban=ban
    
    # def show_privileges (self):
    #     first_name=super().first_name("Kruger")
    #     last_name=super().last_name("shonz")
    #     print ("Hello", first_name,last_name)
    #     print (self.add, self.forbidden, self.ban)

    
user=User()
user.first_name("Arkovich")
user.last_name("Mordovich")
user.info("Loves gaming","fan of night clubs","Cigarettes addictive")
user.describe_user()
# admin=Admin()
# admin.first_name("Genry")
# admin.last_name("Kubets")
# admin.privileges()
# admin.show_privileges()
admin=Admin()
admin.admin.show_privileges()

#3

my_tesla=Electric_car('tesla','models s','2019')
my_tesla.battery.describe_battery()
my_tesla.battery.get_range() 
my_tesla.battery.upgrade_Battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#Importing one class

#24(imports)
from ports import Car

my_new_car=Car("Audi","A4",2018)

print (my_new_car.desryption())

my_new_car.odometr=23
my_new_car.read_metr()

#storing few classes in one module

from ports import Electric_car

tesla=Electric_car("tesla","a4",2019)
tesla.battery.describe_battery()
tesla.battery.get_range()
tesla.battery.upgrade_Battery()
tesla.battery.describe_battery()
tesla.battery.get_range()

#importing few classes from the module

from ports import Car, Electric_car

beetle=Car("Kaz","froggger",2020)
print (beetle.desryption())

bee=Electric_car("Tesla","a4",2222)
print (bee.desryption())

#importing the whole module

import ports

my_bee=ports.Car("Adui","202",1987)
print (my_bee.desryption())

bib=ports.Electric_car("Tesla","truck",1999)
print (bib.desryption())

#importing the whole module

from ports import * #не рекомендуется использовать этот метод, так как могут быть вызваны конфликты с именами в файле

#importing another way 

from ports import Car
from portable import Electric_car

car=Car("Audi","A28",2090)
print (car.desryption())

t_car=Electric_car("Dudi",20,"kariz")
print (t_car.desryption())

#using pseudonyms

from ports import Electric_car as EC

my_tesla=EC("Twka","AE4",2020)
print (my_tesla.desryption())

#Extra tasks
#1
#78 (imoprts)
from ports import Restaurant

rest=Restaurant("kurkih","Asian food")
rest.open_restaurant()

#2
#99 (imports)
from ports import *
admin=Admin()
admin.admin.show_privileges()

#Standard 

from random import randint
x=randint(1,6)
print (x)

from random import choice
players=["Alex","Miranda","Josh","Loie","Loice","Andrew"]
fir=choice(players)
print (fir)

#extra tasks

class Die():
    def __init__(self):
        self.sides=6
    
    def roll_die(self,nub=None):
        if nub==None:
            nub=self.sides

        from random import randint
        x=randint(1,nub)
        print (x)

for i in range(10):
    rub=Die()
    rub.roll_die()

#2

kort=[1,2,3,4,"a",5,"b",6,7,"d","k","r","F",10,100]
jez=[]
from random import choice
for i in range (4):
    x=choice(kort)
    jez.append(x)
for i in jez:
    print (i)

#3

nub=0
win=[4,6,2,1]
jez=[]
while  jez!=win:
    for i in range (4):
        x=choice(kort)
        jez.append(x)
    nub+=1
print (nub-1)

#FILES AND EXCEPTIONS
#reading from the file

with open('text.txt') as file_object: #Сегодня мы будем рассматривать открытие файлов. Начнем с распаковки простого txt файла, как file_object (или другая иная переменная)
    contents=file_object.read() #в переменную контентс мы пихаем все, что было в файле (с помощью метода переменная.read())
print (contents) #После выполнения всех действий с файлом, его надо закрыть, но это не требуется, так как мы прописываем with, что как бы автоматом закрывает файл после всех действий с ним
print (contents.rstrip())# r.strip удаляет все лишние пустые строки в конце

#reading line by line

filename="text.txt"
with open (filename) as file_object:
    for line in file_object:
        print (line.rstrip())

#making a list of lines from the the file

filename="text.txt"
with open (filename) as file_object:
    lines=file_object.readlines() #readlines читает каждую строку (НЕ ПУТАТЬ С readline)
for line in lines:
    print (line.rstrip())

#Working with the context of file

filename="text.txt"
with open (filename) as file_object:
    lines=file_object.readlines() #readlines читает каждую строку (НЕ ПУТАТЬ С readline)

pi_str=" "
for line in lines:
    pi_str+=line.strip()

print (pi_str)
print (len(pi_str))

#Big files: million numbers

filename="text.txt"
with open (filename) as file_object:
    lines=file_object.readlines() 
pi_str=" "
for line in lines:
    pi_str+=line.strip()
print (f"{pi_str[:52]}")
print (len(pi_str))

#Checking Birthday 

filename="text.txt"
with open (filename) as file_object:
    lines=file_object.readlines() 
pi_str=" "
for line in lines:
    pi_str+=line.strip()

birthday=input("Enter your birthday date in the form month day year (without spaces) : ")
if birthday in pi_str:
    print ("Your birthday is in this number")
else:
    print ("your birthday doesn't appear in the first million of pi numbers")

#Extra tasks
#1

with open ("text.txt") as fil:
    for line in fil:
        print (line)

with open ("text.txt") as fil:
    print ("sec method ")
    x=fil.read()
    print (x)

with open ("text.txt") as fil:
    print ("third method")
    lines=fil.readlines()
print (lines)

#2

message="I like dog"
message=message.replace('dog',"cat")
print (message)

with open ("text.txt") as fil:
    for line in fil:
        if "python" in line:
            line=line.replace('python','C')
        print (line)

#write in the empty file
#ВИДЫ ЗАПИСИ В ФАЙЛ -> 'r' - открыть файл в режиме чтения . 'w' - режим записи . 'a' - присоединение . 'r+' - чтение и запись в файл

filen="program.txt"
with open (filen, 'w') as fil:
    fil.write("I love programming")
    

#many lines writing

filen="program.txt"
with open (filen, 'w') as fil:
    fil.write("I love programming\n")
    fil.write('And here is the new line\n') #ADDED THIS LINE

#adding data to the file

with open (filen,'a') as fil:
    fil.write('I know that sounds strange,but still ')
    fil.write('\nOh, hi mark')

#Extra tasks
#1

x=str(input("Hello there, tell me ur name ! :"))
with open ('text.txt', 'a') as fil:
    fil.write(x)

#2

flag=True
while flag:
    x=str(input("Hello, please tell me ur name : "))
    if x!='':
        with open ('program.txt','a') as fil:
            x+="\n"
            fil.write(x)
    else :
        flag=False

#Exception Zero Division error

print (5/0)

#Using try-except

try:
    print (5/0)
except ZeroDivisionError:
    print ("You cant divide by zero")

#using Exceptions to reduce the amount of the emergency situations

print ("give me to numbers and i will divide them\n")
print ("to finish, press enter without entering any text\n")

while True:
    first=input("Enter your first number: ")
    if first=="":
        print ("bye")
        break
    second=input("Enter your second number: ")
    if second=="":
        print ("bye")
        break
    try:
        answ=int(first)/int(second)
    except ZeroDivisionError:
        print ("You can't divide by zero")
    else:
        print (answ)
    
#Analysing and excepting FileNotFound

filename="alice.txt"
try:
    with open (filename, encoding='utf-8') as f:
        content=f.read()
except FileNotFoundError:
    print (f"Sorry, but there is no {filename} in this directory")

#Analysing the whole text

filename="alice.txt"
try:
    with open (filename, encoding='utf-8') as f:
        content=f.read()
except FileNotFoundError:
    print (f"Sorry, but there is no {filename} in this directory")
else:
    words=content.split()
    num=len(words)
    print (f"The file {filename} includes {num} number of words")

#Working with a few files

def count(filename):
    try:
        with open (filename, encoding='utf-8') as f:
            content=f.read()
    except FileNotFoundError:
        print (f"Sorry, but there is no {filename} in this directory")
    else:
        words=content.split()
        num=len(words)
        print (f"The file {filename} includes {num} number of words")

filename="alice.txt"
count(filename)

#Errors without notifications to the user

def count_1(filename):
    try:
        with open (filename, encoding='utf-8') as f:
            content=f.read()
    except FileNotFoundError:
        pass
    else:
        words=content.split()
        num=len(words)
        print (f"The file {filename} includes {num} number of words")

filename="alice.txt"
filen="Mob.txt"
count_1(filename)
count_1(filen)

#Extra Tasks
#1

fir=input("The first number: ")
sec=input("The second number: ")
try:
    x=(int(fir)) + (int(sec))
except ValueError:
    print ("You have words, but no numbers. Dont do it next time !")
else:
    print (x)

#2

while True:
    fir=input("The first number: ")
    sec=input("The second number: ")
    try:
        x=(int(fir)) + (int(sec))
    except ValueError:
        print ("You have words, but no numbers. Dont do it next time !")
    else:
        print (x)
    
    x=input("If you want to stop, just click enter ")
    if x=="":
        break

#3

try:
    with open('alice.txt', encoding='utf-8') as g:
        g=g.read()
    with open ('text.txt', encoding='utf-8') as f:
        f=f.read()
except FileNotFoundError:
    print ("some of the files is missing")
else:
    print (f)
    print (g)

#4

try:
    with open('alice.txt', encoding='utf-8') as g:
        g=g.read()
    with open ('text.txt', encoding='utf-8') as f:
        f=f.read()
except FileNotFoundError:
    pass
else:
    print (f)
    print (g)

#5

line='Row, row, rOw, rrr, ROW'
x=line.lower().count('row')
print (x)

#Saving data by using json
#json.dump() - Получает два аргумента - сохраняемые данные и объект файла
#json.load() - читает список обратно в память

import json

numbers=[2,3,5,7,11,13]
filename='numbers.json'
with open (filename, 'w') as f:
    json.dump(numbers,f)

with open (filename) as f:
    numbers=json.load(f)
print (numbers)

#saving and reading data made by user

username=input("Please input your name : ")
filename='numbers.json'
with open (filename, 'w') as f:
    json.dump(username, f)
    print (f'We will remember u, {username}')

"""Сейчас мы откроем файл и юзанем инфу из него """

filename='numbers.json'
with open (filename) as f:
    username=json.load(f)
    print (f'Welcome back, {username} !!!')

filename="numbers.json"
try:
    with open (filename) as f:
        username=json.load(f)
except FileNotFoundError:
    username=input("Enter your name: ")
    with open (filename, 'w') as f:
        json.dump(username,f)
        print ('We will remember u')
else:
    print (f"welcome back {username}")

# Refactoring

import json

def get_stored():
    filename="numbers.json"
    try:
        with open (filename) as f:
            username=json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def new_user():
    username=input("Please input your name : ")
    filename='numbers.json'
    with open (filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    username=get_stored()
    if username:
        print (f'Love and greet , da supa {username}')
    else:
        username=new_user()
        print (f'We will remember u, {username}')

greet_user()

#Extra tasks
#1

import json

filename='numbers.json'
x=int(input("Введите ваше любимое число: "))
with open (filename, "w") as f:
    json.dump(x,f)

with open (filename) as f:
    x=json.load(f)
    print (f"Я знаю ваше любимое число, это - {x}")

#2

try:
    with open (filename) as f:
        x=json.load(f)
    print (f"Я знаю ваше любимое число, это - {x}")
except FileNotFoundError:
    filename='numbers.json'
    x=int(input("Введите ваше любимое число: "))
    with open (filename, "w") as f:
        json.dump(x,f)

#Test scenario

import unittest

def get_format(first,last):
    full=f'{first} {last}'
    return full.title()

class NamesTest(unittest.TestCase):

    def test_first(self):
        formated=get_format('janis','griffin')
        self.assertEqual(formated, 'Janis Griffin')

if __name__=='__main__':
    unittest.main()

#Test scenario

import unittest

def get_format(first,middle,last=''):
    if last:
        full=f'{first} {middle} {last}'
    else:
        full=f'{first} {middle}'
    return full.title()

class NamesTest(unittest.TestCase):

    def test_first(self):
        formated=get_format('janis','griffin')
        self.assertEqual(formated, 'Janis Griffin')

    def test_sec(self):
        formate=get_format('wolfgang','mozart','amadeus')
        self.assertEqual(formate,'Wolfgang Mozart Amadeus')

if __name__=='__main__':
    unittest.main()

#Extra tasks
#1
import unittest

def country(city,capital):
    fil=f"{city} {capital}"
    return fil.title()

class NamesTest(unittest.TestCase):
    def test_first(self):
        fr=country('moscow','russia')
        self.assertEqual(fr,"Moscow Russia")

if __name__=='__main__':
    unittest.main()

#2
import unittest

def country(city,capital, population=None):
    if population:
        fil=f'{city} {capital} {population}'
    else:
        fil=f"{city} {capital}"
    return fil.title()

class NamesTest(unittest.TestCase):
    def test_first(self):
        fr=country('moscow','russia')
        self.assertEqual(fr,"Moscow Russia")
    
    def test_two(self):
        fr=country('new-York',"usa",'50000000')
        self.assertEqual(fr,'New-York Usa 50000000')

if __name__=='__main__':
    unittest.main()

# assertEqual(a,b) -> a==b
# assertNotEqual (a,b) -> a!=b
# assertTrue(x) -> x==True
# assertFalse(x) -> x==False
# assertIn(element , list) -> проверка , что элемент в списке
# assertNotIn(element , list) -> проверка , что элемент НЕ в списке

#class for testing

import unittest

class Anonym():
    def __init__(self,question):
        self.question=question
        self.responses=[]
    
    def show_question(self):
        print (self.question)
    
    def store_resp(self, new_resp):
        self.responses.append(new_resp)
    
    def show_res(self):
        print ("Survey total : ")
        for i in self.responses:
            print (f'- {i}')

question="What is your first language ?"
my_survey=Anonym(question)
my_survey.show_question()
print ("\t\t\t\t\tPress enter in an empty field to stop the program\n")
while True:
    x=input("So, what you think ? : ")
    if x=='':
        break
    my_survey.store_resp(x)
my_survey.show_res()

class TestAnon(unittest.TestCase):
    def test_store_inf(self):
        question="What is your first language ?"
        my_survey=Anonym(question)
        my_survey.show_question()
        my_survey.store_resp("English")
        self.assertIn('English', my_survey.responses)

    def test_store_three(self):
        question="What is your first language ?"
        my_survey=Anonym(question)
        my_survey.show_question()
        reps=["English","French","Spanish"]
        for i in reps:
            my_survey.store_resp(i)
        for res in reps:
            self.assertIn(res, my_survey.responses)

if __name__=='__main__':
    unittest.main()

#class for testing

import unittest

class Anonym():
    def __init__(self,question):
        self.question=question
        self.responses=[]
    
    def show_question(self):
        print (self.question)
    
    def store_resp(self, new_resp):
        self.responses.append(new_resp)
    
    def show_res(self):
        print ("Survey total : ")
        for i in self.responses:
            print (f'- {i}')

question="What is your first language ?"
my_survey=Anonym(question)
my_survey.show_question()
print ("\t\t\t\t\tPress enter in an empty field to stop the program\n")
while True:
    x=input("So, what you think ? : ")
    if x=='':
        break
    my_survey.store_resp(x)
my_survey.show_res()

class TestAnon(unittest.TestCase):
    def test_store_inf(self):
        question="What is your first language ?"
        my_survey=Anonym(question)
        my_survey.show_question()
        my_survey.store_resp("English")
        self.assertIn('English', my_survey.responses)

    def test_store_three(self):
        question="What is your first language ?"
        my_survey=Anonym(question)
        my_survey.show_question()
        reps=["English","French","Spanish"]
        for i in reps:
            my_survey.store_resp(i)
        for res in reps:
            self.assertIn(res, my_survey.responses)

if __name__=='__main__':
    unittest.main()

#method SetUp()

class TestAnonist(unittest.TestCase):

    def setUp(self):
        question="What is your first language ?"
        self.my_survey=Anonym(question)
        self.responses=['English',"French","Spanish"]
        

    def test_store_inf(self):
        self.my_survey.store_resp(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three(self):
        for response in self.responses:
            self.my_survey.store_resp(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__=='__main__':
    unittest.main()

#Extra Task

import unittest

class Employee():
    def __init__(self, name, lastname, salary):
        self.name=name
        self.lastname=lastname
        self.salary=salary
    
    def give_raise(self, high=5000):
        self.salary+=high
        print (f"Now {self.name} {self.lastname} gets {self.salary} dollars per year ! ")
    
class TestEmp(unittest.TestCase):

    def setUp(self):
        self.emp=Employee("Richard","Gauss",50_000)
        self.REE=55_000
        self.rip=75_000
    
    def test_give_raise_default(self):
        self.emp.give_raise()
        self.assertEqual(self.REE, self.emp.salary)
    
    def test_custom (self):
        self.emp.give_raise(25_000)
        self.assertEqual(self.rip, self.emp.salary)

if __name__=='__main__':
    unittest.main()

THE END OF THE PART 1 
