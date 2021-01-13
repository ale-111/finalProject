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
while i < len(num) - 12:  ### iterate over the digits
    first = int(num[i]) ### each digit will be a variable
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


### Problem 9
for a in range(1, 1000):     ### a has to be smaller than 1ppp
    for b in range(1,1000):   #### b has to be smaller than 1ppp
        c = 1000 - a - b
        if a<b<c:             ### each number must be smaller than the other
            if a**2 + b**2 == c**2:
                print(a*b*c)

### Problem 10

def primecheck(n):                      ### check if a number is a prime number
    for i in range(2, int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True

c = 0
primesum = 0
prime = 1
while c < 2000000:   ### loop until c is smaller than 2 mil
    prime += 1
    if primecheck(prime): ### only add to primesum if prime is a prime number
        primesum += prime
    c += 1
print(primesum)

### Problem 11

grid = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

grid = grid.strip().split('\n') ### splitting the numbers into rows


### create a matriz
mat = [[0 for i in range(20)] for n in range(20)] 

for x in range(0,20):
    k = 0
    for y in range(0,20):
        s = grid[x]
        mat[x][y] = int(s[k]+s[k+1])
        k += 3

def horizontal(mat,j):  ### calculate product of numbers horizontally
    prod = 0
    for i in range(0,16):
        c = 1
        for n in range(0,4):
            c = c*mat[j][i+n]
            if c > prod:
                prod = c
    return prod
