import multiprocessing
import time

# function to calculate large prime numbers using Sieve of Eratosthenes algorithm
def prime_num_cal(n):
    # creating a list of numbers substituted with "True" in place
    range_of_n = [True for x in range(n+1)]
    # Smallest prime number
    p = 2
    while(p*p <= n):
        # If not 'false' then number is not prime
        if (range_of_n[p] == True):
            for i in range(p*p , n+1 , p):
                range_of_n[i] = False
            p = p + 1
    prime_numbers = []
    for i in range(int(n * 0.5), n + 1):
        if (range_of_n[i] == True):
            prime_numbers.append(i)
    return prime_numbers

# calculating the modulus for large numbers
def mod_calculator(num, mod):
    residual = 0
    temp = str(num)
    for i in range(0, len(temp)):
        residual = (residual * 10 + int(temp[i])) % mod
    return residual

# calculating gcd using Euclidean method
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

# calculation of modulo inverse using extended Euclidean method
def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if (x < 0):
        x = x + m0
    return x

# generating prime numbers
prime_num1 = prime_num_cal(200)[-1]
prime_num2 = prime_num_cal(300)[-1]

# calculating 'n' and Euler's totient function
n = prime_num1 * prime_num2
eulers_totient = (prime_num1-1) * (prime_num2-1)

# calculating public key for encryption
for i in range(eulers_totient,int(eulers_totient*0.5),-1):
    if(i%2==1):
        if(gcd(eulers_totient,i)==1):
            public_key=i
            break

# calculating private key for decryption
private_key = modInverse(public_key,eulers_totient)

# creating dictionary of alphabets and their respective positions
alpha = [chr(x) for x in range(ord('a'), ord('z') + 1)]
pos = [x for x in range(1, 27)]
enc_dict = {k:v for (k,v) in zip(alpha, pos)}
dec_dict = {k:v for (k,v) in zip(pos, alpha)}
enc_dict[' '] = 0
dec_dict[0] = ' '

# print(enc_dict,"\n",dec_dict)

def mod_calculator_par(num):
    residual = 0
    temp = str(num)
    for i in range(0, len(temp)):
        residual = (residual * 10 + int(temp[i])) % n
    return residual

inp = "osama was killed"

if __name__ == '__main__':
    # user section
    initial = time.time()
    string = list(inp)
    position_dec, position_enc, enc_text, dec_text = [], [], [], []
    for i in string:
        position_dec.append(enc_dict[i])
position_dec = [pow(x,public_key) for x in position_dec]
p_obj = multiprocessing.Pool()
enc_text = p_obj.map(mod_calculator_par,position_dec)
p_obj.close()
p_obj.join()
dup_enc_text = []
dup_enc_text = [str(x) for x in enc_text]
print("encrypted text : "+''.join(dup_enc_text))
position_enc = [pow(x,private_key) for x in enc_text]
p_obj2 = multiprocessing.Pool()
dec_text = p_obj2.map(mod_calculator_par,position_enc)
p_obj2.close()
p_obj2.join()
dec_text1=[]
for text in dec_text:
    dec_text1.append(dec_dict[text])
print("decrypted text : "+ ''.join(dec_text1))
end = time.time()
print("\ntime elapsed ",end-initial)