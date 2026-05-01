a=int(input("enter First number = "))
b=int(input("Enter Second number = "))
print("1:Add \n 2:sub \n 3:multi \n 4:div")
choice = int(input("enter your choice = "))
if(choice==1):
    res=a+b
    print("Addition = " ,res)
elif(choice==2):
    res=a-b
    print("Subtraction = " ,res)
elif(choice==3):
    res=a*b
    print("Multi = " ,res) 
elif(choice==4):
    res=a/b
    print("Divide = " ,res)     
else:
    print("invaild input")          
