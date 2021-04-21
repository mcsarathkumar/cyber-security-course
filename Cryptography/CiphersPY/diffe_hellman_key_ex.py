import maths

# To take input from the user
q= int(input("Enter a large prime integer (q): ")) #large prime integer

if(maths.prime(q)):
    phi = maths.tot(q)
    print("Below are the primitive root numbers of q:")
    print(phi)

    # To take input from the user
    a = int(input("Enter a primitive root number (a) mod q; a < q : "))  #primitive root mod q; a < q

    if a in phi:
        # To take input from the user
        xa = int(input("secret key (xa) of A where xa < q : ")) #secret key of A; xa < q
        if(xa<q):
            #public key of A send to B
            ya = (a**xa) % q
            print("public key of A send to B: ",ya)
        else:
            print("secret key of A; xa >= q")
        
        # To take input from the user
        xb = int(input("secret key (xb) of B where xb < q : ")) #secret key of B; xb < q
        if(xb<q):
            #public key of B send to A
            yb = (a**xb) % q
            print("public key of B send to A: ",yb)
        else:
            print("secret key of B; xB >= q")
   
        #actual logic for computing key
        kab = (a**(xa*xb)) % q
        print("actual key is : ",kab)
   
        #B computed key
        kb = (ya**xb) % q
        print("B computed key: ",kb)
   
        #A computed key
        ka = (yb**xa) % q
        print("A computed key: ",ka)
    else:
        print(a,"primitive root mod ",q,"; ",a," < ",q)   