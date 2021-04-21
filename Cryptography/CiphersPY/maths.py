import math

# Finding gcd
def gcd(a, b): 
    a, b = max(a, b), min(a, b) 
    c = 1 
    while c: 
        c = a % b 
        a = b 
        b = c 
    return a 

# Euclidean Algorithm
def tot(n): 
    phi = [] 
    x = 1 
    while x < n:        
        # not for x in xrange(n) because the input is too big for xrange 
        if gcd(x, n) == 1:             
            phi += [x] 
            x += 1 
        else:
            x += 1 
    return phi

# function for Extended Euclidean Algorithm
def gcdExtended(a, b):    
    # Base Case
    if(a==0):        
        return b, 0, 1
	    
    gcd,x1,y1 = gcdExtended(b%a, a)
    # Update x and y using results of recursive
    # call    
    x = y1 - (b//a) * x1
    y = x1    
    return gcd,x,y

# Finding Inverse using Extended Euclidean Algorithm
def inverseOf(b, a):
    # Driver code   
    n = a
    gcd,x,y = gcdExtended(a, b) 
    print("gcd: ",gcd,"x: ",x,"y: ",y)   
    if (y<0 or y>n):
        y=y%n
    return y

# checking for prime
def prime(n):    
    # checking for less than 1
    if n <= 1:
        print(n,"is not a prime number")
        return False
    # checking for 2
    elif n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        print(n,"is not a prime number")
        return False
    else:
        # iterating loop till square root of n
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            # checking for factor
            if n % i == 0:
                print(n,"is not a prime number")
                print(i,"times",n//i,"is",n)
                # return False
                return False
        # returning True
        return True