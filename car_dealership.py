car = {'honda':4000, 'toyota':3000, 'ford': 2000, 'acura': 7000}
print car


class account:
    def __init__(self, balance=0):
            self.balance = balance
    def withdraw(self, amount):
        self.balance -= amount

my_account = account(3500)# Object called my_account is = to the class called account where 
print my_account.balance # you want to use stuff from (like balance).

# the for loop allows the appendage of a new key:value (car:price) to the dictionary w/o
#having to create an entire new set of conditional statements.car[brand] is the cost of a specific car.
for brand in car.keys(): 
    if my_account.balance >= car[brand]:
        print "I can afford the " + brand
    else:
        print "I need to make $" + str(car[brand] - my_account.balance) + " more to buy the " + brand 


def qstn():
    answer = raw_input("Would you be interested in buying a car?")
    print answer

  #  answer = 'no' or 'yes'
    if answer == "yes":
        print raw_input("Here are the cars and their assigned prices ('Press Enter'):")
        for brand in car.keys():
            print "The " + brand + " costs $" + str(car[brand]) + "."

        answer2 = None # its called None bc the buyer cannot purchase a car that DNE or that is too expensive for them.
        while answer2 == None:
            answer2 = raw_input("Which one would you want?")
            if answer2 not in car.keys():
                print "Sorry, we don't have that here, please try again."
                answer2 = None
            elif car[answer2] > my_account.balance:
                print "Sorry, you cannot afford the car."
                answer2 = None
            else:  
                my_account.withdraw(car[answer2])            
                print "You have a " + str(answer2)
                print "You have " + str(my_account.balance) + " left."
                print "Thank you! Drive safely!"
        
    elif answer == "no":
        print raw_input("Good bye! Have a nice day!")
        
        
    
print qstn()    

    
  
















