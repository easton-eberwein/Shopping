##
## Name: Easton Eberwein
## Prog9Eberwein.py
##
## Purpose: This program lets us exercise the concept of an array of objects. 
##
## Inputs: The inputs are the intial file to read in, which number from the menu to choose from, an item's name, quantity and price, an item to be searched for
##
## Outputs: The outputs are telling the user an item has been added to the list, telling the user an item has been deleted from the list, printing the items in a list, if you have a certain item in the list, the total number of items in the list, the total cost of the items in the list, whether or not the list is empty, telling the user the list has been cleared, and saying goodbye.
##
## Certification of Authenticity:
##
## I certify that this lab is entirely my own work
##



#function to add an item to the list, asking the user to add the item name, quantity, and unit price
def addItem(currentList):
    item= input("Please enter the item name: ")
    quantity= int(input("Please enter the quantity of the item: "))
    price= float(input("Please enter the unit price of the item: $"))
    theItem= Item(item, quantity, price)
    print(item,"has been added to the list.")

    #return the item to be appended to the list in main
    return theItem


#loop through each item in the list and print each item, as long as there is at least one item in the list.
def printEachItem(listToBePrinted):

    if len(listToBePrinted)>0:
        
        for i in range(len(listToBePrinted)):
            print("Item number [", i,"] is", listToBePrinted[i])

    else:
        print("The list is empty.")
        print()


#loop through the list and see if the user entered item is in the list, making sure there is at least one item in the list.
def findItemInList(listOfItems, name, number, cost):
    if len(listOfItems)==0:
        print("There are no items in the cart.")
        print()

    else:
        target= str(input("Please enter the item you wish to find: "))
        print()
        count=0
        for i in range (len(listOfItems)):
            if listOfItems[i].getName()==str(target):
                count+=1
                quantityOfItem= listOfItems[i].getQuantity()
                thePrice= listOfItems[i].getPrice()
                priceOfItem= float(thePrice)

        if count>0:
            print("Yes you have", quantityOfItem, target, "at ${:,.2f}".format(priceOfItem), "each.")

        else:
            print("The item", target,"is not in the cart.")
                
        print()


#loop through the list and count how many different items, and total items there are.
def countItems(items):
    count=0
    quantityOfItems=0
    for i in range(len(items)):
        count+=1
        quantityOfItems+= items[i].getQuantity()

    print("There are", count, "different items in the cart. There is a total of", quantityOfItems,"items in the cart.")
    print()


#calculate the total cost of all the items, quantity times unit price, and add them all together.
def totalCostOfAllItems(price):
    cost=0
    for i in range(len(price)):
        units= price[i].getQuantity()
        eachCost= price[i].getPrice()
        pricePerItem= units*eachCost
        cost+= pricePerItem

    return cost


#see if the list is empty or not and tell the user.
def determineIfListIsEmpty(items):
    if len(items)==0:
        print("The list is empty.")
    else:
        print("The list is not empty. There are",len(items),"different items in the list.")

    print()


#clear the whole list and tell the user the list is empty
def clearTheList(items):
    items.clear()
    print("The list is now empty.")
    print()


#delete a certain item from the list
def deleteItemFromList(items):

    #intialize count as the length of items
    count= len(items)

    #ask the user for the item they want to delete
    delete= str(input("Please input the item to be deleted: "))
    count-=1

    #loop through the list one less than the list length. If you loop the actual list length an idexing error will occur.  
    for i in range(count):
        if items[i].getName()==str(delete):
            items.remove(items[i])

            #tell the user the item has been removed and add 1 to count to make sure the last message isn't printed.
            print(delete,"has been removed from the list.")
            count+=1

    #since we looped through one less than the list length we have to check to see if the last item in the list is the one to be deleted and if it is, delete it.
    if items[-1].getName()==str(delete):
        items.remove(items[-1])
        print(delete,"has been removed from the list.")
        count+=1

    #if count is one less than the list, this message will be printed saying the item is not in the list.
    if count==len(items)-1:
        print(delete,"is not in the list.")
        
    print()

#import the class
from itemEberwein import Item

def main():

    #initialize variables that need to be intialized
    itemName= 0
    quantity= 0
    price= 0
    itemList= [ ]
    theItem= Item(itemName, quantity, price)

    #open the file
    fileName= input("Please enter the name of the file: ")
    print()
    theFile= open(fileName, "r")
    numInputs= int(theFile.readline())

    #assign certain lines of the file to certain variables and then add each item to the list
    for i in range (numInputs):
        itemName= str(theFile.readline().rstrip())
        quantity= int(theFile.readline())
        price= float(theFile.readline())
        theItem= Item(itemName, quantity, price)
        itemList.append(theItem)


    #greet the user
    print("Hello user! This program will give you 9 different choices to choose from!")
    print()

    #initialize choice and then use a while loop to allow the user to choose from the menu until they choose 0.
    choice= -1
    while (choice !="0" ):
        print("Please choose from the menu below")
        print("1. Add an item to the list")
        print("2. Delete an item from the list")
        print("3. Print each item in the list")
        print("4. Search for a user-specified item in the list")
        print("5. Count the total number of items in the list")
        print("6. Total the cost of the items in the list")
        print("7. Determine whether the list is empty")
        print("8. Clear the list")
        print("0. Quit")
        print()

        choice= str(input("Please enter your choice: "))

        print()

        #if the choice is one, call the itemBeingAdded function and then append what is returned to the list.
        if (choice=="1"):
            itemBeingAdded= addItem(itemList)
            itemList.append(itemBeingAdded)
            print()

        #if the choice is 2, then call the function deleteItemFromList and delete the item that the user chooses.
        elif (choice=="2"):
            deleteItemFromList(itemList)

        #if the choice is 3, call the function printEachItem, and then print each item from the list.
        elif (choice=="3"):
            printEachItem(itemList)

        #if the choice is 4, call the function findItemInList, and search for the item in the list that the user inputs.
        elif (choice=="4"):
            findItemInList(itemList, itemName, quantity, price)

        #if the choice is 5, call the function countItems, which will count the items in the list and output it.
        elif (choice=="5"):
            countItems(itemList)

        #if the choice is 6, call the function totalCost, which will calculate the toal cost, return the cost, and then the cost will be formatted
        elif (choice=="6"):
            totalCost= totalCostOfAllItems(itemList)
            print("The total cost is: ${:,.2f}".format(totalCost))
            print()

        #if the choice is 7, call the function determineIfListIsEmpty, which will loop through the list and determine if the list is empty.
        elif (choice=="7"):
            determineIfListIsEmpty(itemList)

        #if the choice is 8, tcall the function clearTheList, which will clear the list.
        elif (choice=="8"):
            clearTheList(itemList)

        #if the choice is 0, print goodbye, and the program ends
        elif (choice=="0"):
            print("Goodbye!")

        #if the choice is anything but 1, 2, 3, 4, 5, 6, 7, or 8, an invalid choice message will output and the user will be asked to input a number between 0-8.
        else:
            print("Invalid choice")
            print()

    #close the file
    theFile.close()

main()
