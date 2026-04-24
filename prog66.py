letter=input("enter a letter:")
if(letter.isupper()):
    print("uppercase")
elif(letter.islower()):
    print("lowercase")
elif(letter.isdigit()):
    print("number")
else:
    print("invalid")