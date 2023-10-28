# files = open('./text.txt')
 
# for line in files:
#     print(line)
    
    
# files.seek(0)
# lineLIst = files.readline()
# print(lineLIst)
    




# files.seek(50)
# paragraph = files.read(100)
# print(paragraph)


# files.close() 


with open('./text.txt') as files:
    for line in files:
        print(line)