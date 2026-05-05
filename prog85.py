side1=int(input("enter side length (in cm):"))
side2=int(input("enter side length (in cm):"))
side3=int(input("enter side length (in cm):"))
if(side1==side2==side3):
    print("equilateral")
elif(side1==side2 or side2==side3 or side3==side1 or side1==side3):
    print("isosceles")
else:
    print("scalene")
