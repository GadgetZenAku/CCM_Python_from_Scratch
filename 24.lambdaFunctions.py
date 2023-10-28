# expression တစ်ခုကိုပဲ auto return ပြန်ပေးတဲ့ method

# def add(n1,n2):
#     return n1 + n2

# print(add(4,5)) #ဒါမျိုးမသုံးသင့် function တစ်ခုအတွက် လုပ်‌ဆောင်စရာနည်းလွန်း

add = lambda n1,n2:n1+n2 # variable'add' become function like above

print(add(5,4))

nums = [1,2,3,4,5,6,7,8,9,10]
# evenNum = list(filter(lambda num:(num%2)==0,nums)) # it is hard to understand
# print(evenNum)
    
print(list(map(lambda num:num*2,nums))) # it is more easy to know
