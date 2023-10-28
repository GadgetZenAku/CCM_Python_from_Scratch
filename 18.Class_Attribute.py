class Car : 
    sterringWheel = 1 # class level attribute တိုက်ရိုက်အသုံးချလို့ရ
    def __init__(self,name,wheels):
        self.name = name # instinct level attribute
        self.wheels = wheels # instinct level attribute
        
    def drive(self): # instinct method
        print(f'{self.name} is driving.') 
        
    #@classmethod # class level methodတည်ဆောက်ချင်ရင်ရေးတဲ့ပုံစံ
    
    @classmethod
    def common(cls): #class လို့နာမည်မပေးရ
        print(f'all car have only {cls.sterringWheel} sterring wheel')
        
# print(Car.sterringWheel)
# Car.common() # တန်းပြီးအသုံးချလို့ရ

lambo = Car('lambogani',4)
print(lambo.sterringWheel)
print(lambo.common())