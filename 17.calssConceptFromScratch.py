# name = 'Htoo Aung Kang'
# print(type(name)) #class object method=function blueprint

#print(name.upper())

# own class

# class Car : 
#     def __init__(self):
#         self.name = 'Lamborghini'
#         self.wheels = 4
        
#     def drive(self):
#         print(f'{self.name} is driving.') 
# lambo=Car()
# # print(lambo.name)
# # print(lambo.wheels)
# lambo.drive()


class Car : 
    def __init__(self,name,wheels):
        self.name = name
        self.wheels = wheels
        
    def drive(self):
        print(f'{self.name} is driving.') 
lambo=Car('lambogani','4')
# print(lambo.name)
# print(lambo.wheels)
lambo.drive()
        
toyota=Car('Toyota','6')
toyota.drive()