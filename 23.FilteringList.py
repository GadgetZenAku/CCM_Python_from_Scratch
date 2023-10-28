nums = [1,2,3,4,5,6,7,8,9,10]
# def even(num):
#     return num%2 == 0

# evenNum = list(filter(even,nums))
# print(evenNum)


#map မူလ list ကိုအခြေခံ item တစ်ခုချင်းစီကို ပြောင်းလဲချင်ရင်

# filter က လိုချင်တဲ့အချို့တစ်ဝက်ကိုပဲ ပြောင်းလဲချင်တာ

# nums = [num for num in nums if (num%2)==0]
# print(nums)

evenNums = []

for num in nums:
    if num%2 == 0:
        evenNums.append(num)
        
print(evenNums)

