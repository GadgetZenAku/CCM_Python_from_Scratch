#'' "" string

#/n string escape or double code in single code use

greet = "hello"
print(greet[0])
print(greet[2])
print(greet[-1])

#slide
print(greet[0:2])# 0 is inclusive, 2 is exclusive အမြဲတမ်း တစ်ခုလျှော့ပေးရ
print(greet[3:5])
print(greet[2:-1])


#add
str1 = 'Hey'
str2 = 'Python'

print(str1+str2)

print(str1 +' '+str2)

print(str1*4)

#some method
#everthing is object in Python. There is many methods. 

# object ပြီးရင် ' . ' ပြီးရင် method 
#example Upper  and  Lower

greet = 'Hello'
greet=greet.upper() # overw2rite
print(greet)


#Split 

names = 'aung,kyaw,su,pa,htoo'
names = names.split(',')
print(names) #list type output


#len
print(len(names))
print(len(greet))