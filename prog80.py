num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
num3=int(input("enter a number:"))
if(num1>(num2 and num3)):
    print("num1 is greatest")
elif(num2>(num1 and num3)):
    print("num2 is greatest")
else:
    print("num3 is greatest")