with open('./text.txt','w') as file: # w ရေးခြင်း
    file.write('I am Htoo Aung Kaung')
    
# another work

with open('./text.txt','a') as file: #a ပေါင်းထည့်
    file. write('i m in 25 years.')
    
list = ['I am now Geologist.']
with open('./text.txt','a') as file:
    file.writelines(list)