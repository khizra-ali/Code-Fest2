'''Create a function that validates a password to conform to the following rules: 
  
#    Length between 6 and 24 characters. 
#    At least one uppercase letter (A-Z). 
#    At least one lowercase letter (a-z). 
#    At least one digit (0-9). 
#    Maximum of 2 repeated characters. '''

def password_checker():
    special_characters = ["!","@","#","$","%","^","&","*","_","(",")","=","+","{","}",":",";","'","?","<",".",",",">"]
    value = True
    input_pass=input("Enter Password: ")
    while value:
        if len(input_pass) < 6:
            print("Length should be greater than 6")
            value=False
            continue
        elif len(input_pass) >= 24:
            print("Length should be not greater than 24")
            value=False
            continue
        elif not any(char.isdigit() for char in input_pass): 
            print('Password should have at least one numeral') 
            value = False    
            continue
        elif not any(char.isupper() for char in input_pass): 
            print('Password should have at least one uppercase letter') 
            value = False  
            continue    
        elif not any(char.islower() for char in input_pass): 
            print('Password should have at least one lowercase letter') 
            value = False
            continue
        elif not any(char in special_characters for char in input_pass):
            print('Password should have at least one special chracter')
            value= False
            continue
        for char in input_pass:
            if char*3:
                value=False
                print("Invalid Passowrd-Maximum two characters can be used")
                break
        else:
            return value
            print("Valid Password")
            break
password_checker()
