names = ['Pan Yaung Chel','Shwe Thamee','Htet Htet Linn Latt','Sara Fish']

for name in names:
    print (name)
    
for name in names:
    if name == 'Pan Yaung Chel':
        print(f'{name} is most adorable.')
    else :
        print(f'{name}are less than her.' )
        
for name in names:
    if name == 'Pan Yaung Chel':
        print(f'{name} is most adorable')
        break # stop here if true
    else :
        print(f'{name}are less than her.' )
        
        
fruits = ['Apple','Waterball','Coconut']

for fruit in fruits:
    print(f'{fruit} is fruit')