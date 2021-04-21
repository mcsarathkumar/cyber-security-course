def get_input1():
    global pt, letter_dict
    pt = input('Please provide plain text to encrypt: ')
    letter_dict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

def get_input2():
    global key
    key = int(input('Please provide a valid key between 0 to 25: ')) 
    check_input2()

def main():
    print("Welcome to Caesar Cipher Cryptography!")  
    get_input1()
    get_input2()

# function to return key for any value
def get_key(val):
    global letter_dict
    for key, value in letter_dict.items():
         if val == value:
             return key
    
def encrypt(pt_input, key):
    ct_input = (pt_input + key) % 26
    return ct_input

def decrypt(ct_input, key):
    pt_input = (ct_input - key) % 26
    return pt_input
    
def check_input2():
    global pt, key, letter_dict
    if (key < 0 or key > 25):
        get_input2()
    else:
        ct = ""
        for l in pt:
            pt_input = letter_dict[l.casefold()]
            ct += get_key(encrypt(pt_input, key))
        print('Cipher text: '+ct)
        decrypt_option = input('Do you want to decrypt the cipher text ? (Yes/No)')
        if decrypt_option.casefold() in ["yes", "y"]:
            actual_pt = ""
            for l in ct:
                ct_input = letter_dict[l.casefold()]
                actual_pt += get_key(decrypt(ct_input, key))
            print('Plain text: '+actual_pt)
            main_option = input('Do you wish to continue Caesar Cipher Cryptography ? (Yes/No)')
            if main_option.casefold() in ["yes", "y"]:
                main()
            else:
                print("Thank you for using Caesar Cipher Cryptography!")  
        else:
            print("Thank you for using Caesar Cipher Cryptography!")
main()