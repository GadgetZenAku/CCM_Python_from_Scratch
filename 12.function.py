# def greet(name,Time): #parameter
#     print(f'Hello,{name}!.Good{Time}')#{dinimically}
    
# greet('Panyaung','Morning')

#default parameter
#function argument and something input patameter

def greet(name='PanYauung',time='Morning'):  #Panyaung and Morning are default parameter
    print(f'Good {time},{name}')
    
greet()

greet(name='STM',time='Midnight')

