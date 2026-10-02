num=[21,34,12,78,56,32,90,65,14,55]

min=num[0]
max=num[0]

for i in num:
    if(i<min):
        min=i
    if(i>max):
        max=i

print(min,max)        
