list=[23,45,67,23,89,90,56,23]
part=23

for num in list:
    if(num==part):
        list.remove(num)

for num in list:
    print(num)