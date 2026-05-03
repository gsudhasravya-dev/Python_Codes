marks=float(input("enter your marks:"))
if(marks>=90):
    print("A")
elif(80<=marks<=89):
    print("B")
elif(70<=marks<=79):
    print("C")
elif(0<=marks<=70):
    print("fail")
else:
    print("invalid marks")