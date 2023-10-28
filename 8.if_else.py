age = int(input('age:'))

if age < 18 :
    print(' u are young.')
elif age >18 and age<30:
    print(' u r in best age')
else:
    print (' u r adult')
    
tired = input('are u tired?"y/n"')

if tired == 'y' and 'Y':
    print('take rest')
elif tired == 'n' and 'N':
    print('Go Ahead')
else:
    print('R u kidding me right now?')
