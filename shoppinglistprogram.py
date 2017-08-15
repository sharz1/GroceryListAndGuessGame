#Python version 3.5.2

#Author Sharlee Bryan

'''
Description: Creates a shopping list for the grocery store and plays a quick guessing game
for the total price of the shopping trip, determining a winner based on closest guess.
 A starter list is provided that can be added in full or part to the shopping list.
 Shopping time is calculated based on time list completed and shopping cart total entered.
'''

from datetime import datetime


def start_menu(player1="",player2=""):
    #Assign a string to a variable
    player1 = input("Enter name of first shopper: ").capitalize()
    player2 = input("Enter name of second shopper: ").capitalize()
    #Use logical operator "and"
    if player1 !="" and player2 !="":
        #Use print and .format() notation to print out the variable assigned
        print("\nThanks {} and {}! Let's create a shopping list!".format(player1,player2))
        shopping(player1,player2)
    else:
        noname=True
        #use a while loop
        while noname:
            #use conditional statements if,elif,else
            if player1=="":
                player1=input("Enter name of first shopper: ").capitalize()
            elif player2=="":
                player2 = input("Enter name of second shopper: ").capitalize()
            else:
                noname=False      
    

def shopping(player1,player2):
    print("\nHere's some options to get you started:")
    #create a tuple and iterate through w/ for loop to print each item on a new line
    st_tup=("1. Milk","2. Eggs","3. Bread","4. Cheese")
    for i in st_tup:
        print(i)
    print("\nEnter a number above to add one of these items to shopping list.")
    print("Enter 5 to add ALL of these to shopping list.")
    #Assign an integer to a variable
    shoplistnum=0
    shoplist_item=""
    shoplist=[]
    #use "not" logical operator
    while not(shoplistnum == 7):
        print("\nEnter 6 to add SOMETHING ELSE to shopping list.")
        print("Enter 7 if the list is complete.")
        print("Enter 8 to remove an item from this list.")
        while True:
            try:
                shoplistnum = int(input("\nEnter number: "))
                if shoplistnum in range(1,9):
                    break
            except:
                print("That is not a valid selection. Please enter a number 1-8")
        #Use "or" operator
        if shoplistnum < 5 or shoplistnum == 6:
            #Call the function that returns a string and print result to the shell
            shoplist_item = get_list_item(st_tup,shoplistnum,shoplist_item,shoplist)
            shoplist.append(shoplist_item)
        elif shoplistnum == 5:
            #converts the starter tuple to a list so it can be appended
            shoplist = list(st_tup)
            #removes first 3 characters (line numbers) from each item in shoplist
            for idx, item in itr_list(shoplist):
                shoplist[idx] = item[3: ]
        elif shoplistnum == 8:
            while True:
                try:
                    remove_item = input("\nWhich item would you like to remove? ").capitalize()
                    shoplist.remove(remove_item)
                    break
                except:
                    print("That item is not on the list. Please enter the item you'd like to remove.")
        print("\nHere is your list so far:")
        #Create a list and iterate through w/ for loop to print each item on a new line
        for i in shoplist:
            print(i)
    guess_game(player1,player2,shoplist)


#iterates through list (for removing line numbers from shoplist)
def itr_list(sequence, start=0):
    for elem in sequence:
        yield start, elem
        #Use "+=" operator
        start += 1       


#define a function that returns a string variable       
def get_list_item(st_tup,shoplistnum,shoplist_item,shoplist):
    if shoplistnum == 6:
        #use "=" operator
        shoplist_item = input("\nEnter name of item you'd like to add. ").capitalize()
    else:
        #decrementing shoplistnum to get list item by index
        shoplistnum -= 1
        shoplist_item = st_tup[shoplistnum]
        #removing first 3 characters (line number) from shoplist_item
        shoplist_item = shoplist_item[3: ]
    
    return shoplist_item   
    
def guess_game(player1,player2,shoplist):

    start_time = datetime.now()

    #Assign a float to a variable
    p1_guess = float(input("\n{}, enter your guess for the total price of the shopping cart: ".format(player1)))
    p2_guess = float(input("\n{}, enter your guess for the total price of the shopping cart: ".format(player2)))
    #Use "*" operator
    comp_guess =(len(shoplist)*2.75)
    #Use "+" operator
    print("\nComputer guess: " + str(comp_guess))
    actual_total = float(input("\nEnter the final total of the shopping cart at checkout: "))

    finish_time = datetime.now()

    #Use "-" operator
    p1_diff = abs(actual_total - p1_guess)
    p2_diff = abs(actual_total - p2_guess)
    comp_diff = abs(actual_total - comp_guess)
    closest=min(p1_diff,p2_diff,comp_diff)
    guesses = {p1_diff:player1,p2_diff:player2,comp_diff:"Computer"}
    winner = guesses[closest]
    print("\nWinner with the closest guess: " + winner + "!!")

    time_diff = finish_time - start_time

    #convert time_diff to minutes and seconds
    minutes = (time_diff.days*86400 + time_diff.seconds)//60
    #Use "/" operator
    hours = minutes//60
    #Use "%" operator
    minutes = minutes%60
    seconds = (time_diff.days*86400 + time_diff.seconds)%60
    print("Your total shoptime: {} hours, {} minutes, {} seconds".format(hours,minutes,seconds))

if __name__ == "__main__":
    start_menu()  


