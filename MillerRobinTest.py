import random
def mrTest(m,n,orgm):
    a=random.randrange(1,n-1)
    count=0
    while True:
        count+=1
        b0=pow(a,m,n)
        if b0==n-1:
            return True
        if b0==1:
            return False

        m=2
        a=b0
        if count>10:
            m=orgm
            a=random.randrange(1,n-1)

while True:
    n=int(input())
    powerOfTwo=0
    while (n-1)%2**powerOfTwo==0:
        powerOfTwo+=1
    powerOfTwo-=1
    m=int((n-1)/2**powerOfTwo)
    orgm=m
    a=mrTest(m,n,orgm)
    b=mrTest(m,n,orgm)
    if not a and not b:
        print("Composite")
    else:
        print("Prime")




    
# import random

# def miller_rabin_test(n, k=5):
#     # If n is less than 2, it's not prime
#     if n < 2:
#         return False
#     # Check if n is 2 or 3, both are prime
#     if n in (2, 3):
#         return True
#     # If n is even, it's not prime
#     if n % 2 == 0:
#         return False

#     # Write n-1 as d * 2^r
#     r = 0
#     d = n - 1
#     while d % 2 == 0:
#         d //= 2
#         r += 1

#     # Perform k rounds of testing
#     for _ in range(k):
#         # Pick a random integer in [2, n - 2]
#         a = random.randint(2, n - 2)
#         x = pow(a, d, n)  # Compute a^d % n

#         if x == 1 or x == n - 1:
#             continue

#         for _ in range(r - 1):
#             x = pow(x, 2, n)
#             if x == n - 1:
#                 break
#         else:
#             return False
#     return True

# # Main program
# while True:
#     n = int(input("Enter a number (or 0 to stop): "))
#     if n == 0:
#         break
#     if miller_rabin_test(n):
#         print("Prime")
#     else:
#         print("Composite")
