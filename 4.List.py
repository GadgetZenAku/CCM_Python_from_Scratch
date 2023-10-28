# [ ] list ','

num = [1,2,3,4,5,6,7]
print(num[1])
print(num[-1])
print(num[1:6])

#combine
num1 = [11,22,33,44]
num2 = [55,66,77,88]
print(num1+num2)

#index change
num = [1,3,3]
num[1] = 2
print(num)

#method
#add (apoend)
num.append(4) # add in the last
print(num)

#(pop)
num.pop() #last one is removed
print(num)

# remove (by name)
nUm = [12,55,44.865,1,2,3,4,5,6,85]
nUm.remove(12)
print (nUm)


#delete
del(nUm[0]) # delete by index, one of use is it can delete by slide

print(nUm)

del(nUm[0:2])
print(nUm)

# list ထဲမှာ List တွေထပ် assign လို့ရ
lL12 = ['htoo',1,1.2,[7,8,9]]

print(lL12)

print(lL12[3])

print(lL12[3][2])





