username=input("Enter username: ")
password=input("Enter password: ")
if password=="123":
    
        print("your  success login!\n")
        print("log in now")
        
        admin=input("Eneter username admin:")
        
        try:
            passAdmin=int(input("Enter a password: "))
            if passAdmin==12345:
            
                    
                    
                    print("Correct password!")
                    print("your accountis create successfully!")
                            
            
                
            else:
                    print("You not admin!")
        except:
            print("your password is not interger!")
   
       
else:
    print("Invalid password")
    
   