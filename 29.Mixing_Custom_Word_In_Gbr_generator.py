words = ['reason','idiots','Iron cross','Big Bag','eternal Gosh','The ants']


from random import randint
def randomSentenseGenerator(word):
    randomIndex = randint(0,len(words)-1)
    return f'{words[randomIndex]} {word}'
with open ('./text.txt') as file:
    paragraph = file.read()
    wordlists = paragraph.split()
    sentenseList = list(map(randomSentenseGenerator,wordlists))
    
    paraCount = int(input('paragraph count :'))
    for count in range(paraCount):
        with open('./genator.txt','a') as write_file:
            write_file.write(''.join(sentenseList)+'\n\n')