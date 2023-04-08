#serial Implementation of RSA algorithm to generate large prime numbers
import time
# function to calculate large prime numbers using Seive of eratosthenes algorithm
def prime_num_cal(n):
    # creating a list of numbers substituted with "True" in place
    range_of_n = [True for x in range(n+1)]
    #Smallest prime number
    p=2
    while(p*p <= n):
        # If not 'false' then number is not prime
        if (range_of_n[p] == True):
            for i in range(p*p , n+1 , p):
                #Marking 'True' for the multiple of 'P'
                range_of_n[i]=False
        p=p+1
    prime_numbers=[]
    for i in range(int(n*0.5),n+1):
        if(range_of_n[i]==True):
            prime_numbers.append(i)
    return prime_numbers
    # calculating the modulus for large numbers
def mod_calculator(num,mod):
    residual = 0
    temp = str(num)
    for i in range(0,len(temp)):
        residual = (residual*10 + int(temp[i]))%mod
    return residual
# calculating gcd using euclidian method
def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a,a)
    # calculation of modulo inverse using extended euclidian method
def modInverse(a, m) :
    m0 = m
    y = 0
    x = 1
    if (m == 1) :
        return 0
    while (a > 1) :
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if (x < 0) :
        x = x + m0
        return x
# generating prime numbers
prime_num1 = prime_num_cal(200)[-1]
prime_num2 = prime_num_cal(300)[-1]
# calculating 'n' and euler's totient function
n= prime_num1 * prime_num2
eulers_totient = (prime_num1-1) * (prime_num2-1)
# calculating public key for encryption
for i in range(eulers_totient,int(eulers_totient*0.5),-1):
    if(i%2==1):
        if(gcd(eulers_totient,i)==1):
            public_key=i
            break
# calculating private key for decryption
private_key = (modInverse(public_key,eulers_totient))
# creating dictionary of alphabets and there resp positions
alpha = [chr(x) for x in range(ord('a'), ord('z') + 1)]
pos = [x for x in range(1,27)]
enc_dict = {k:v for (k,v) in zip(alpha,pos)}
dec_dict = {k:v for (k,v) in zip(pos,alpha)}
enc_dict[' ']= 0
dec_dict[0]=' '
#print(enc_dict,"\n",dec_dict)
# user section
initial = time.time()
inp = "aditya was mathematician is "
position,enc_text,dec_text = [],[],[]
for i in inp:
    position.append(enc_dict[i])
for i in position:
    enc_text.append(str(mod_calculator(pow(i,public_key),n)))
print("\nencrypted text : "+''.join(enc_text)+"\n")
for i in enc_text:
    dec_text.append(dec_dict[mod_calculator(pow(int(i),private_key),n)])
print("decrypted text : "+''.join(dec_text))
end = time.time()
print("\ntime elapsed ",end-initial)