from PIL import Image
import math
letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",",",".","!","?"," "]
number = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56"]

def Encode(img, msg, lst): #image,plaintext,X
    global L
    L = []
    length=len(msg)
    if length > 255:
        print("Text too long! (don't exeed 255 characters)")
        return False
    if img.mode != 'RGB':
        print("Image mode needs to be RGB")
        return False
    # Making deep copy of image to make encryption! with original image intact
    encoded_img = img.copy()
    width, height = img.size
    index = 0 #1
    for row in range(height): #0
        for col in range(width): #1x
            r, g, b = img.getpixel((col, row))
            if row == 0 and col == 0 and index < length:
                asc = length
            elif index <= length:
                c = lst[index - 1]
                asc = c // 255
                # Storing remainder value, used for decoding
                L += [c % 255]
            else:
                asc = r
            encoded_img.putpixel((col, row), (asc, g, b))
            index += 1
    return encoded_img


# Decode function of Steganography

def Decode(img):
    global L
    width, height = img.size
    msg = ""
    lst = []
    index = 0
    length = 0
    for row in range(height):
        for col in range(width):
            try:
                r, g, b = img.getpixel((col, row))
            except ValueError:
                r, g, b, a = img.getpixel((col, row))
            if row == 0 and col == 0:
                length = r
            elif index <= length:
                lst += [r * 255 + L[index - 1]]
            index += 1
    return lst

def cipher(num,e):
    for i in range(len(num)):
        X.append((int(num[i])**e)%n)

def decipher(num,d):
    for i in range(len(num)):
        Y.append((int(num[i])**d)%n)

def gcd(a, b):
    while b != 0:
        (a, b)=(b, a % b)
    return a

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

def modInverse(a, m):
     
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1


n = 493
e = 13
d=modInverse(e,phi(n))

def Decrypt(encoded_image_file):
    global i,j,Y

    Y=[]
    img2 = Image.open(encoded_image_file)
    #print(img2, img2.mode)
    hidden_text = Decode(img2)
    print(hidden_text)
    decipher(hidden_text,d)
    print(Y)
    numD=[]
    for i in range(len(Y)):
        for j in range(len(number)):
            if(Y[i]==int(number[j])):
                numD.append(letter[j])
    print(numD)
    for i in numD:
        print(i,end="")
    print("\n")



def Encrypt(original_image_file,encoded_image_file):
# encrypts a plaintext message using the current key
    global plaintext, numC, j, X
    X=[]
    plaintext = (input("Enter Plaintext :"))
    '''plaintext = (plaintext.lower())'''
    numC = []
    for i in range(len(plaintext)):
        for j in range(len(letter)):
            if(plaintext[i]==letter[j]):
                numC.append(number[j])
    cipher(numC,e)
    print("Ciphertext:", X)
    print("Number of Ciphertext blocks:", len(X))
    img = Image.open(original_image_file)
    #print(img, img.mode)
    img_encoded = Encode(img, plaintext, X)
    #print(img_encoded)
    if img_encoded:
        img_encoded.save(encoded_image_file)
        print("{} saved!".format(encoded_image_file))