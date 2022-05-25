import random
import math

letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
          "v",
          "w", "x", "y", "z", ",", ".", "!", "?", " "]
number = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
          "18",
          "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]


#a funcrtion to generate a prime number
def get_prime():
    prime = []
    for num in range(1000, 10000 + 1):
        # prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):   #2=> num-1
                if (num % i) == 0:
                    break
            else:
                prime.append(num)
    y = len(prime)
    x = random.randint(1, y-1)
    return prime[x]



def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

# A function that returns Euler's Totient
#phi = (p-1)(q-1)
# but in this code we're calcukating phi by counting how many numbers are co-prime with n
def phi(n):
    amount = 0
    for k in range(1, n):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

#function for encryption
def cipher(num, e):
    # num: list of plain letters' adjacent numbers
    # e: encryption key
    for i in range(len(num)):
        X.append((int(num[i]) ** e) % n)


def decipher(num, d):
    for i in range(len(num)):
        Y.append((int(num[i]) ** d) % n)




def Encrypt():
    # encrypts a plaintext message using the current key
    global plaintext, numC, j, X
    X = []  #a list to store the cipher text
    plaintext = (input("Enter Plaintext :"))  #take an i/p from the user which is the plain text
    plaintext = (plaintext.lower())
    numC = []  # a list to store the adjacent number for each letter of the plaintext
    for i in range(len(plaintext)):
        for j in range(len(letter)):
            if (plaintext[i] == letter[j]):
                numC.append(number[j])
    cipher(numC, e)
    print("Ciphertext:", X)


def Decrypt():
    global i,j,Y
    Y=[]

    hidden_text =  (input("Enter cipher text :"))
    print(hidden_text)
    decipher(hidden_text,d)
    numD=[]
    for i in range(len(Y)):
        for j in range(len(number)):
            if(Y[i]==int(number[j])):
                numD.append(letter[j])
    for i in numD:
        print(i,end="")
    print("\n")

p= 43
q= 59
n = 2537
e = 13
d = 937
if __name__ == '__main__':
    print("To redefine n,e, or d, type 'n','e','d','p','q'... etc.")
    print("To encrypt a message with the current key, type 'Encrypt'")
    print("To decrypt a message with the current key, type 'Decrypt'")
    print("Type quit to exit")
    print('\n')
    print('\n')
mm = str()
mm = str()

if mm.lower() == 'encrypt':
    Encrypt()
elif mm.lower() == 'decrypt':
        Decrypt()
elif mm.lower() == 'n':
    try:
        print('current n = ', n)
        n1 = get_prime()

        n = n1
        print('n set to :', n)
    except:
        print('invalid')

elif mm.lower() == 'p':
    try:
        print('current p = ', p)
        p1 = get_prime()
        if p1!= q:
         p= p1
         print('p set to :', p)
    except:
         print('invalid')

elif mm.lower() == 'q':
    try:
        print('current q = ', q)
        q1 = get_prime()
        if q1!= p:
         q= q1
         print('q set to :', q)
    except:
         print('invalid')

elif mm.lower() == 'help':
    print("To redefine n,e, or d, type 'n','e',... etc.")
    print("To encrypt a message with the current key, type 'Encrypt'")
    print("Type quit to exit")
    print('\n')
    print('\n')

elif mm.lower() == 'e':
    try:
        print('current e = ', e)
        e1 = int(input(" Enter a value for e :"))
        if e1 < 2 or math.gcd(phi(n), e1) != 1:
            print('Invalid input')
        else:
            e = e1
            print('e set to :', e)
    except ValueError:
        print('please enter a number')

elif mm.lower() == 'd':
    try:
        print('current d = ', d)
        d1 = int(input(" Enter a value for d :"))
        # For Finding D: It must satisfies this property:-  (D*E)Mod(eulerTotient)=1;
        if d1 <= 0 and (e * d1) % phi(n) != 1:
            print('Invalid input')
        else:
            d = d1
            print('d set to :', d)
    except ValueError:
        print('please enter a number')


def getciphertext():
    return str(X)



