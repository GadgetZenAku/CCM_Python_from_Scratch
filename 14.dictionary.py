# {} dictionary

person={
    'name':'Pan Yaung Chel', # , မေ့လို့ error တက်နေဖူးခဲ့
    'age' : 29
}
print(person['name'])# list ထဲက value တွေကို ဆွဲထုတ်ချင်ရင်‌ရေးတဲ့ပုံစံ

person['hair coloir']='golden'

# print(person)

# print(name in person) # name ဆိုတဲ့ key ကို person ဆိုတဲ့ Dict ထဲမှာရှိမရှိမေး ရှိရင် True မရှိရင် False

# if 'name' in person :
#     print('it's work)

# if 'nothing' in person:
#     print("It's work")
# else:
#     print('No')

personKeys = list(person.keys()) # list type casting from dictionary for key
personValue = list(person.values())
    
print(personKeys)
print(personValue)