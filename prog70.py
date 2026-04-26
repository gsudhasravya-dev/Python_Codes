mon_num=int(input("enter month number:"))
if mon_num in[1,3,5,7,8,10,12]:
    print("31")
elif(mon_num==2):
    print("28 or 29")
elif mon_num in [4,6,9,11]:
    print("30")
else:
    print("not valid: only 12 months")