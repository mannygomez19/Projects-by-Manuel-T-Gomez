print("Welcome to the argument-validity test!")       

def premises_conclusion():
    
    premises_1 = raw_input("Premises: ")
    premises_qstn = raw_input("Would you like an additional premises(yes/no)? ")
    
    while premises_qstn.isalpha():
        
        while premises_qstn == 'yes':
            
            premises_1 = raw_input("Premises: ")
            premises_qstn = raw_input("Would you like an additional premises(yes/no)? ")

            
        if premises_qstn == 'no':
            break

        while premises_qstn != 'yes' or premises_qstn != 'no':
            print("Please enter yes or no.")
            premises_qstn = raw_input("Would you like an additional premises(yes/no)? ")
            if premises_qstn == 'yes' or premises_qstn == 'no':
                break
        
    conclusion = raw_input("Conclusion: ")

    
premises_conclusion()
                                 
