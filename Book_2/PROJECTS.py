#import this #Remove the fitst "hashtag" to see the truth
#Password manager


PASSWORDS= {'email':'Dummy_text@mail.gmail.com',
            'blog':'Password_is_here',
            'luggage':12345}

import sys, pyperclip
if len(sys.argv) < 2:
    print ('Использование [имя учетной записи] - копирование пароля учетной записи')
    sys.exit()

account=sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print (f'Пароль для {account} скопирован в буфер')
else:
    print ("Учетная запись отсутствует")


#Project
import pyperclip
text=pyperclip.paste()

lines=text.split('\n')
for i in range (len(lines)):
    lines[i]='* '+lines[i]

text='\n'.join(lines)
pyperclip.copy(text)



#Project
def isPhonenumber(text):
    if len(text) !=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    
    if text[3] !='-':
        return False
    
    for i in range (4,7):
        if not text[i].isdecimal():
            return False
    
    if text[7] !='-':
        return False
    
    for i in range (8,12):
        if not text[i].isdecimal():
            return False
    
    return True
print (isPhonenumber('415-555-4242'))
print (isPhonenumber("grow"))



#Project
