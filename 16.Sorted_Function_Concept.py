# nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,30]

# SORTED
# print(sorted(nums))

# names = ['htoo Aung kaung','Hlaig Min Than','kyaw kyaw','BoBo','Bago']
# print(sorted(names)) first Caps, Sec a to z

nums = [1,2,3,4,8,9,5,11,48,51,21,12,2,4,8,]

# for num in nums:
#     print(nums)

#Set တူတာတွေကို တစ်ခါပဲပြမယ် sorting တော့လုပ်မပေးရ
# for num in set(nums):
#     print(num)


person = {}
while True:
    name = input('Name : ')
    age = input('Age: ')
    person[name] = age
    another = input('Another : y or n?')
    if another == 'y':
        continue
    else:
        break
print(person)

agesList = list(person.values())
# print(ages)
for age in set(agesList):
    # print(age) 
    count = agesList.count(age)
    print(f'{age} years old {count}')
