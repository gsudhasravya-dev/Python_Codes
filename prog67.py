temp=float(input("enter temperature:"))
if(temp<15):
    print("COLD")
elif(15<temp<25):
    print("WARM")
elif(temp>25):
    print("HOT")
else:
    print("invalid temperature")