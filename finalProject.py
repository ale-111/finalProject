### Project Euler problem 1

sum = 0 

for i in range(1000):    ### for every number below 1000
    if i%3 == 0 or i%5 == 0: ### if number is divisible by 3 or 5
        sum += i

print(sum)

### Problem 2

a = 1
b = 2
c = 0

sum = 2 ### first even number is 2

while c <= 4000000: 
    c = a + b
    if c%2 == 0: ### if number is divisible by 2, add number to sum
        sum += c
    a = b   ### next number in the sequence
    b = c

print(sum)

### Problem 3 

def find_factor(num):
    f = 2
    for i in range (0, num): ### for every number between 0 and num
        if f >= num:        ### factor cannot be larger than num
            break
        elif num%f == 0:        ### check if its a factor
            num = num/f
        else:
            f += 1              ### move to next num
    return f
print(find_factor(600851475143))

### Problem 4

def check_pallindrome(num):     ### check if num is a pallindrome
    s = str(num)
    for i in range (1, len(s)//2 + 1):
        if s[i-1] != s[-i]:
            return False
    return True

large_num = 0

for l in range(100, 1000):
    for k in range(l, 1000):
        if check_pallindrome(l*k):      ### if num is a pallindrome
            if l*k > large_num:         ### find product of two nums
                large_num = l*k

print(large_num)


### Problem 5

def div(num):               ### check if a number is divisible by 1-20
    for i in range(11,21):      
        if num % i == 0:    ### check if num is divisible by i 
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    num = 2
    while not div(num):         ### loop and add 1 to num until num is divisible by 1-20
        num += 1  
    print(num)

### Problem 6
sum1 = 0
for i in range(1,101):  ### find the sum of the squares of the first one hundred natural numbers
    sum1 += i**2

sum2 = 0

for n in range(1,101):   ### find the square of the sum of the first one hundred natural numbers
    sum2 += n
sum2 = sum2**2

print(sum2-sum1) 

### Problem 7

def primecheck(n):                      ### check if a number is a prime number
    for i in range(2, int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True

def findprime(n):
    cprime = 0          ### count for prime number
    primenum = 1        
    while cprime < n:   ### loop until count for prime number = n
        primenum += 1
        if primecheck(primenum): ### only add 1 to cprime if primenum is a prime number
            cprime += 1
    return primenum

print(findprime(10001))

### problem 8 

num = '\
73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'

greatest = 0
i = 0
while i < len(num) - 12:
    first = int(num[i]) 
    sec = int(num[i+1]) 
    thi = int(num[i+2]) 
    fo = int(num[i+3]) 
    fiv = int(num[i+4]) 
    six = int(num[i+5]) 
    sev = int(num[i+6]) 
    eight = int(num[i+7])
    nine = int(num[i+8])  
    ten = int(num[i+9]) 
    elev = int(num[i+10])
    twel = int(num[i+11])
    thir = int(num[i+12])

    product =  first*sec*thi*fo*fiv*six*sev*eight*nine*ten*elev*twel*thir

    if product > greatest:
        greatest = product
    i += 1
print(greatest)  



    