num=int(input("enter a number:"))
if(num%3==0 and num%5==0):
    print("multiple of both")
elif(num%3==0):
    print("multiple of 3")
elif(num%5==0):
    print("multiple of 5")
elif(num%3==0 and num%5==0):
    print("multiple of both")
else:
    print("not a multiple of any")