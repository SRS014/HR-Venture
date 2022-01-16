
#First Code

print("Choose the operation, which operation do you perform?\n1.Addition.\n2.Subtraction.\n3.Multiplication.\n4.Division.")
operation = int(input("Enter which operation do you want: "))

num1 = int(input("Enter the Number1: ")) 
num2 = int(input("Enter the Number2: "))

if(operation==1):    
    result = num1+num2
elif(operation==2):    
    result = num1-num2
elif(operation==3):    
    result = num1*num2
elif(operation==4):    
    result = num1/num2
else:
    res = num1%num2

print("The Result is:", result)