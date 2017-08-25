stock = {'Apples': [0, .5, 0], 'Bananas': [0, .25, 0]}

def directory():
    print("Press 1 to check inventory count of stock items")
    print("Press 2 to prices on stock item")
    print("Press 3 to Revenues")
    return input("Please select an action: ")

run = directory()

#Uses to sort Inventory menu
def Inventory():
    print("Press 1 to add new inventory item")
    print("Press 2 to remove current inventory item")
    print("Press 3 to add amount to current inventory item")
    print("Press 4 to exit")
    return input("Please select an action: ")

def LowerCaseKeys():
    LStock = dict((k.lower(), v) for k,v in stock.items())
    return LStock    
while True:
    #Select Options from Directory
    if run == '1' or run == '2' or run == '3':
        #Activates Function dependent on the selection
        if run == '1':
            for key in stock.keys():
                print("{} : {} Remaining".format(key, stock[key][0]))
            option = Inventory()
            if option == '1':
                Item = input("What is the name of the item you would like to add: ")
                while True:
                    try:
                        Quantity = int(input("How many do you have? "))
                        Price = int(input("What price?"))
                        Revenue = int(input("How much revenue is made by this item: "))
                        stock[Item] = [Quantity, Price, Revenue]
                        print("Action Complete")
                    except ValueError:
                        print("Not Valid Input")
                     
            elif option == '2':
                Removal = input("What item would you like to remove: ")
                if Removal in stock:
                    stock.pop(Removal, None)
                else:
                    print("Item not in stock list")
            elif option == '3':
                Item = input("What item would you like to add more of (Start with Uppercase): ")              
                if Item in stock:
                    Add = int(input("How many of this item would you like to add: "))
                    stock[Item][0] += Add
                else:
                    print("Item not in List")
            elif option == '4':
                break
            else:
                print("Not valid option")
                option = Inventory()
        elif run == '2':
            for key in stock.keys():
                print("{} : ${}".format(key, stock[key][1]))
                #alter prices
            answer = input("Would you like to change prices: ").lower()
            if answer == 'yes':
                Item = input("What item would you like to change(Start with Uppercase): ")              
                if Item in stock:
                    Price = float(input("New Price: "))
                    stock[Item][1] = Price
                else:
                    print("Item not in List")
        elif run == '3':
            for key in stock.keys():
                print("{} : {}".format(key, stock[key][2]))
            answer = input("Would you like to change prices: ").lower()
            if answer == 'yes':
                Item = input("What item's revenue would you like to change (Start with Uppercase): ")              
                if Item in stock:
                    Add = int(input("How much revenue did this item make: "))
                    stock[Item][2] += Add
                else:
                    print("Item not in List")
            elif answer == 'no':
                break
        else:
            print("Insert Valid Value")

        #Gives User Option to search Directory again
        answer = input("Would you like to search again? Yes or No: ").lower()
        while (answer != 'yes' and answer != 'no'):
            #If input not Yes or No, then make user try again
            print("Please Try Again.")
            answer = input("Would you like to search again? Yes or No: ").lower()
        if answer == 'yes':
            run = directory()
        elif answer == 'no':
            break
    #If input is not within the directory, then repeat until User enters valid input
    else:
        print("Please enter valid input")
        run = directory()
            

