person={}

# name = input('name:')
# age = input('age :')

# person[name]=age #name is key, age is value
# print(person)

while True:
    name = input('name:')
    age = input('age :')
    person[name]=age #name is key, age is value
    
    another = input('Another y/n: ')
    if another == 'y':
        continue
    else:
        break
print(person)

# dictionary တစ်ခုကို တန်းပြီး Loop ပတ်လို့မရဘူး

for (key,value) in person.items(): # ,items နဲ့ ဆွဲထုတ်ပြီး loop ပတ်
    print(f'{key} is {value} years old.')