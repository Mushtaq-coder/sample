#Name: Mushtaq
#Heros inventory Program

#Initialize the inventory with some items 
inventory = ["sword", "armor", "shield", "healing potion"]
print("Hello world")
print("hello world")
print("Mushtaq")
#define the menu options as a mutiline string
menu_options = """These are your options:
                   1 - Show inventory
                   2 - add item to the inventory
                   3 - number of items in the inventory
                   4 - remove item from the inventory
                   5 - swap item in the inventory for a different item at position"""

#Display a welcome message
print("Welcome! I am here to help you manage your inventory")

#infinite loop to continually prompt the user for options 
while True:
    option = input("\nWhat would you like to do? Enter i to see the options, q to quit ")
    
    #if the user wants to quit
    if option.lower()== 'q':
        print("Goodbye!")
        break
    
    #Display the menu options 
    elif option == 'i':
        print(menu_options)
    
    #Print the current inventory 
    elif option == '1':
        print("This is your inventory"," , ".join(inventory))
    
    #Add a new item to the inventory
    elif option == '2':
        item = input("Enter the item you want to add: ")
        inventory.append(item)
        print("Item",item," has been added to the inventory.")
    
    #Display the number of items in the inventory
    elif option == '3':
        count = len(inventory)
        print("The number of items in the inventory is:",count)
    
    #Remove an item from the inventory 
    elif option == '4':
        item = input("Please enter the item you would like to remove: ")
        
        #this will check if the item is in inventory then it will remove 
        if item in inventory:
            inventory.remove(item)
            print("item",item," has been removed from the inventory.")
            
        else:
            print("Item",item," is not in the inventory.")
    
    #Swap an item in the inventory with a different item at a specified position
    elif option == '5':
        item_to_replace = input("Enter the item you want to replace: ")
        item_to_add = input("Enter the item you want to add: ")
        
        # this will check item is in the inventory 
        if item_to_replace in inventory:
            
            #find the index of the item to replace
            index = inventory.index(item_to_replace)
            
            #replace the item at the specified index with new item
            inventory[index] = item_to_add 
            print("Item ",item_to_replace," has been replaced with",item_to_add, "in the inventory.")
            
        else:
            print("Item ",item_to_replace," is not in the inventory.")
            
    # if user enters invalid option 
    else:
        print("please enter 1-5 for options or q for quit")

#Print a message  
print("\nGoodbye!")

