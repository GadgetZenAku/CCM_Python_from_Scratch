class RestaurantTable:
    
    menus = {
        'Pizza' : 5000,
        'Cola' : 600,
        'Apple Juice' : 2000,
        'Humburgar' : 1000,
        'Fried Potato' : 1500
    } # class level attribute
    
    # class activated 
    def __init__(self) :
        self.total = 0
        self.orders = []
        
    def addOrder(self,order):
        self.orders.append(order)
        self.total += self.menus[order] #ဒီနေရာလေးကိုသိပ်မရှင်းဘူးဖြစ် 
        
    def printBill(self):
        for order in self.orders:
            print(f'{order} : {self.menus[order]}')
        print(f'Total price is {self.total}')
            
            
def startProgram():
    table = RestaurantTable()
    while True:
        order=input('order :')
        table.addOrder(order)
        another = input('Order again? y/n : ')
        if another == 'y' and 'Y':
            continue
        if another == 'n' and 'N':
            table.printBill()
        break

startProgram()