# functions

def isPrime(x):
    for i in range (2, x/2):
        if (x%i == 0):
            #print str(x) + " IS NOT prime"
            print x,"IS NOT a prime number"
            break
    else:
        #print str(x) + " IS a prime number"
        print x, "IS a prime number"


num = 1
while(num > 0):
    num = input("Enter the number: ")
    if (num == 0):
        break
    isPrime(int(num))

print "Exiting ..."

