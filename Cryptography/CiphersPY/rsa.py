import maths
        
# To take input from the user
p = int(input("Enter a prime integer (p): ")) #prime integer

# To take input from the user
q = int(input("Enter a prime integer (q): ")) #prime integer

if( maths.prime(p) and maths.prime(q) ):
    #compute n
    n = p*q
    print("n = p*q = ",p,"*",q," = ",n)

    #compute phi_n
    phi_n = (p-1)*(q-1)
    print("phi_n = (p-1)*(q-1) = (",p,"-1)*(",q,"-1) = ",phi_n)

    #compute primitive roots of phi_n
    phi = maths.tot(phi_n)
    print("Below are the primitive root numbers of phi_n:")
    print(phi)

    # To take input from the user
    e = int(input("Enter a primitive root number (e) mod phi_n; e < phi_n : "))  #primitive root mod phi_n; e < phi_n

    if e in phi:    
        print("public key is : <",e,",",n,">")            
        d = maths.inverseOf(e, phi_n)
        print("private key is : <",d,",",n,">")
    else:
        print(e,"primitive root mod ",phi_n,"; ",e," < ",phi_n)    