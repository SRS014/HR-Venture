#Program
j = 1
psd = "open@door"
while(j>0):
    print("Choose Your Option. What You want to do?\n1. Open The Door?.\n2. Reset Password?\n3. Exit?")
    
    temp = int(input("Enter The Option: "))
    

    if(temp == 1):
        i = 0
        while(i < 3): 
            print('\nEnter The Door Password: ')
            inp = input()
            if(inp == psd):
                print("Opened The Door Succesfully!")
                break
            else:
                print("Incorrect Password! Try Again.")
            i = i+1    
        else:
            print("\nAutomatically Locked The Door!\n")

    elif(temp == 2):
        
        print("\nGive some information: \n1. User Name.\n2. Mobile No.")
        User_Name = 'Sohan'
        Mob = 1773008535
        
        s = 1
        while(s>0):
            UserName = input("\nEnter User Name No: ")
            MobNo = int(input("\nEnter Mobile No: "))
            if(User_Name == UserName and Mob == MobNo):
                NewPass = input("\nEnter New Password: ")
                ConfiNewPass = input("\nEnter Confirm New Password: ")
                
                if(NewPass == ConfiNewPass):
                
                    temp = NewPass
                    NewPass = ConfiNewPass
                    ConfiNewPass = temp

                    psd = temp
                print("Password Reset Successfully!")
                break
                
            else:
                print("Incorret User Name and Mobile No.")
            s = s+1
        
    elif(temp == 3):
        print("Exit From 'Smart Door Lock System!'")
        break
    j = j+1 