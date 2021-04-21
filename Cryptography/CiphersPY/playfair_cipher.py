import string
import itertools

def get_inputs():    
    global case, plaintext, key, alphabets    
    case = input("please choose either lowercase or uppercase: ")
    plaintext = input("Please provide the plain text: ")
    key = input("Please provide the key for play fair cipher encryption: ")
    alphabets = ""
    if case.casefold() in ["uppercase","upper","u","up"]:
        alphabets += string.ascii_uppercase.replace('J', 'I')
        plaintext = plaintext.replace('j', 'i').upper()
        key = key.upper().replace('J', 'I')
        case = 'uppercase'
    else:
        alphabets += string.ascii_lowercase.replace('j', 'i')
        plaintext = plaintext.replace('j', 'i').casefold()
        key = key.casefold().replace('j', 'i')
        case = 'lowercase'    

def key_matrix(key, alphabets):            
    slots = []
    for x in itertools.chain(key, alphabets):
        if not x in slots: slots.append(x)
    matrix = list(slots[i:i+5] for i in range(0, 25, 5))   
    return matrix

def convert_case(letter):
    if case == 'uppercase':
        letter = letter.upper()
    else:
        letter = letter.casefold()
    return letter
    
def digraphs(plaintext):         
    new_plaintext=[]
    while len(plaintext)>0:
        new_plaintxt = plaintext[:2]       
        if (len(new_plaintxt) == 1) or (new_plaintxt[0]==new_plaintxt[1]):
            if (new_plaintxt!=convert_case('x')):
                new_plaintxt=new_plaintxt[0]+convert_case('x')
                new_plaintext.append(new_plaintxt)
                plaintext=plaintext[1:]
            elif (new_plaintxt!=convert_case('z')):
                new_plaintext=new_plaintxt[0]+convert_case('z')
                new_plaintext.append(new_plaintxt)
                plaintext=plaintext[1:]
        else:            
            new_plaintext.append(new_plaintxt)
            plaintext=plaintext[2:]   
    return new_plaintext

def get_coords(digraph, matrix):    
    coords = []
    for char in digraph:
        for x in range(5):
            for y in range(5):                
                if matrix[x][y] == char:
                    coords.append((x, y))
    return coords

def encrypt(matrix, new_plaintext):
    ciphertext = ""
    for digraph in new_plaintext:
        coords=get_coords(digraph, matrix)        
        if coords[0][0] == coords[1][0]:
            letter_1_x, letter_1_y = ((coords[0][0], (coords[0][1] + 1) % 5))
            letter_2_x, letter_2_y = ((coords[1][0], (coords[1][1] + 1) % 5))        
        elif coords[0][1] == coords[1][1]:
            letter_1_x, letter_1_y = (((coords[0][0] + 1) % 5), coords[0][1])
            letter_2_x, letter_2_y = (((coords[1][0] + 1) % 5), coords[1][1])
        else:
            letter_1_x, letter_1_y = (coords[0][0], coords[1][1])
            letter_2_x, letter_2_y = (coords[1][0], coords[0][1])
        ciphertext+=matrix[letter_1_x][letter_1_y]+matrix[letter_2_x][letter_2_y]
    return ciphertext

def decrypt(matrix, new_ciphertext):
    deciphertext = ""
    for digraph in new_ciphertext:
        coords=get_coords(digraph, matrix)        
        if coords[0][0] == coords[1][0]:
            letter_1_x, letter_1_y = ((coords[0][0], (coords[0][1] - 1) % 5))
            letter_2_x, letter_2_y = ((coords[1][0], (coords[1][1] - 1) % 5))        
        elif coords[0][1] == coords[1][1]:
            letter_1_x, letter_1_y = (((coords[0][0] - 1) % 5), coords[0][1])
            letter_2_x, letter_2_y = (((coords[1][0] - 1) % 5), coords[1][1])
        else:
            letter_1_x, letter_1_y = (coords[0][0], coords[1][1])
            letter_2_x, letter_2_y = (coords[1][0], coords[0][1])
        deciphertext+=matrix[letter_1_x][letter_1_y]+matrix[letter_2_x][letter_2_y]
    return deciphertext

if __name__ == '__main__':
    get_inputs()
    if(plaintext, key, alphabets):
        matrix = key_matrix(key, alphabets)
        new_plaintext = digraphs(plaintext.replace(" ", ""))                
        ciphertext = encrypt(matrix, new_plaintext)        
        new_ciphertext = digraphs(ciphertext)
        deciphertext = decrypt(matrix, new_ciphertext)
        print("deciphertext: ",deciphertext,"ciphertext: ", ciphertext)