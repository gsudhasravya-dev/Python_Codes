a=int(input("enter a number:"))
b=int(input("enter other number:"))
operator=input("enter a operator:")
if(operator=="+"):
    print(a+b)
elif(operator=="-"):
    print("a-b=",a-b)
    print("b-a=",b-a)
elif(operator=="*"):
    print(a*b)
elif(operator=="/"):
    print("a/b=",a/b)
    print("b/a=",b/a)
elif(operator=="**"):
    print("a**b=",a**b)
    print("b**a=",b**a)
else:
    print("invalid operator")

