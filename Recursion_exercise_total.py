# 1

def recurse(n):
    a = 0
    for i in range(1 , n + 1):
        a += 1 / i
    print(f"{a:.5f}")

n = int(input())
if n <= 0:
    print("N must be a positive number")
else:
    recurse(n)



# 2

def recurse(a):
    um = 0
    dau = 1
    for i in range(1, a + 1):
        sum += dau / i
        dau *= -1
    print(f"{sum:.5f}")

a = int(input())
if a <= 0:
    print("N must be a positive number")
else:
    recurse(a)



#3
def demo(N):
    if N==0:
        return 1
    else:
        return (1 + 1/N**2)*(demo(N-1))

N = int(input())
if N < 1:
    print("N is must possitive number")
else:
    print(demo(N))



#4

def giai_thua(n):
    if n==1:
        return 1
    else:
        return n*giai_thua(n-1)
def demo(x,N):
    if N==0:
        return 1
    else:
        return (x**N/giai_thua(N)) + demo(x,N-1)


x = int(input())
N = int(input())
if N<1:
    print("N is must positive number")
else:
    print(demo(x,N))


# 5

def  finite_geometric_series (n,r, sum = 0.0):
    if n <= 0 or r <= 0:
        print("N must be a positive number")
    else:
        for i in range(n):
            sum += r**i
    print( f'{sum:.5f}')


r, n = (input().split(' '))
n = int(n)
r = float(r)

sum = finite_geometric_series (n,r)


#6
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_series(n, sum=0):
    if n <= 0:
        print("N must be a positive number")
    else:
        sum = 0
        for i in range(1, n + 1):
            sum += factorial(i)
        print(sum)

n = int(input())
factorial_series(n)


# 7
def sum_square(n):
    if n <= 0:
        return 'N is must positive number'
    else:
        sum2 = 0
        for i in range(1, n+1):
            sum2 += (i**2)
        return sum2

try:
    n = int(input())  
    print(sum_square(n))
except ValueError:
    print('N is must positive number')


#8

def multiple_odd(n):
    if n <= 0:
        return 'N is must positive number'
    else:
        mul = 1
        for i in range(1,2*n,2):
                mul = mul*i
        return mul 

try:       
    n = int(input())
    print(multiple_odd(n))
except ValueError:
    print('N is must positive number')


#bai 9
def finite_arithmetic_sequence():
    try:
        a, d, N = map(int,input().split())
        
        if N <= 0:
            return "N is must positive number"
        
        sum_seq = 0
        for i in range(N):
            sum_seq += a + i * d
        return f"{sum_seq}"
    
    except ValueError:
        return "Enter a valid integer."

print(finite_arithmetic_sequence())




#bai 10
def finite_exponential_series():
    try:
        a, N = map(int,input().split()) 
        
        if N <= 0:
            return "N is must positive number"
        
        sum_seq = 0
        for i in range(1, N + 1):
            sum_seq += a ** i
        return f"{sum_seq}"
    
    except ValueError:
        return "Enter a valid integer."

print(finite_exponential_series())
