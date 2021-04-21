import random
def get_input1():
    global pt, plaintext
    pt = input('Please provide plain text to encrypt: ')
    plaintext = []
    for i in pt:
        plaintext.append(i.casefold())
    
def get_input2():
    global key
    key=[]
    for i in range(97,123):
        key.append(chr(i))
    random.shuffle(key)

def main():
    print("Welcome to Monoalphabetic Cipher!")  
    get_input1()
    get_input2()
    get_encrypt_key()
    encrypt_decrypt()

def get_encrypt_key():
    global plaintext, key, letter_dict
    letter_dict={}
    for key, val in zip(plaintext, key): 
        letter_dict[key] = val 
    
def get_decrypt_key(val):
    global letter_dict
    for key, value in letter_dict.items():
        if val == value:
            return key
    return "key doesn't exist"
    
def encrypt_decrypt():
    global pt, key, letter_dict    
    ct = ""
    for l in pt:
        ct += letter_dict[l.casefold()]    
    print('Cipher text: '+ct)
    decrypt_option = input('Do you want to decrypt the cipher text ? (Yes/No)')
    if decrypt_option.casefold() in ["yes", "y"]:
        actual_pt = ""
        for l in ct:
            actual_pt += get_decrypt_key(l)         
        print('Plain text: '+actual_pt)
        main_option = input('Do you wish to continue Monoalphabetic Cipher ? (Yes/No)')
        if main_option.casefold() in ["yes", "y"]:
            main()
        else:
            print("Thank you for using Monoalphabetic Cipher!")       

main()