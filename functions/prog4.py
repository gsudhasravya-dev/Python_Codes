def check_prime(num):
    for i in range(2,num):
        if(num%i==0):
            print("not prime")
            return
    
    print("prime")

check_prime(10)
