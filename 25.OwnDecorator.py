# သာမန် function မလုပ်ခင် ကြိုပြီး လုပ်ဆောင်ထားလို့ရ 
def greet(fun):
    def wrapper():
        print('Hello')
        fun()
        print('Good Morning')
    return wrapper
@greet
def sayName():
    print('Pan Yaung')
    
sayName()

def greet(fun):
    def wrapper(name):
        print('Hello')
        fun(name)
        print('Good Morning')
    return wrapper
@greet #decorator
def sayName(name):
    print(name)
    
sayName('Htoo Aung Kaung')