#Global
name = 'Pan Yaung Chel1'

def sayMyname():
    #Local
    global name #like type variable
    name = 'Pan Yaung Chel2'
    print(name)
    
sayMyname()
print(name)