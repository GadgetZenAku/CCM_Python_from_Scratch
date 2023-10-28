# list တွေကို overwrite ဖြစ်အောင်သုံး

nums = [2,5,6,7,8,9,10,20,30,15]

#map(function,list)
def mapfunction(num):
    return num*2
    
print(list(map(mapfunction,nums)))

# map က ပိုပြီး မြင်သာ လွယ်ကူသလိုခံစားရ

nums = [num*2 for num in nums]
print(nums)