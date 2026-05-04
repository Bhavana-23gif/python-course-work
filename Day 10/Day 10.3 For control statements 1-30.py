n = int(input("Enter N: "))
for i in range(1, n+1):
    print(i)

n = int(input("Enter N: "))
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)

n = int(input("Enter N: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print("Sum =", sum)

n = int(input("Enter N: "))
for i in range(1, n+1):
    if i % 2 != 0:
        print(i)

n = int(input("Enter N: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print("Factorial =", fact)

n = int(input("Enter N: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

n = int(input("Enter N: "))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count = count + 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")

n = int(input("Enter number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
print("Sum of digits =", sum)

n = int(input("Enter N: "))
a = 0
b = 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

n = int(input("Enter N: "))
count = 0
for i in range(1, n+1):
    if i % 3 == 0:
        count = count + 1
print("Count =", count)

n = int(input("Enter number: "))
temp = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

n = int(input("Enter N: "))
for i in range(1, n+1):
    if i % 5 == 0:
        print(i)

a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))
max = a
for i in range(1):
    if b > max:
        max = b
    if c > max:
        max = c
print("Maximum =", max)

n = int(input("Enter number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reverse =", rev)

n = int(input("Enter N: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print("Sum =", sum)

n = int(input("Enter N: "))
while n >= 1:
    print(n)
    n = n - 1

n = int(input("Enter N: "))
sum = 0
for num in range(2, n+1):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        sum = sum + num
print("Sum of primes =", sum)

n = int(input("Enter number: "))
product = 1
while n > 0:
    digit = n % 10
    product = product * digit
    n = n // 10
print("Product =", product)

n = int(input("Enter N: "))
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

a = int(input("Enter a: "))      #GCD
b = int(input("Enter b: "))
fact=[]
for i in range(1,a+1):
    if a%i==0 and b%i==0:
        fact.append(i)
print(fact[-1])  


n = int(input("Enter N: "))
for i in range(1, n+1):
     print("*" * i)

n = int(input("Enter N: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

n = int(input("Enter N: "))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum = sum + i
if sum == n:
    print("Perfect")
else:
    print("Not Perfect")

n = int(input("Enter number: "))
count = 0
while n > 0:
    count = count + 1
    n = n // 10
print("Digits =", count)

n = int(input("Enter N: "))
for i in range(1, n+1):
    if i % 7 == 0:
        print(i)

#LCM of 1 number:
b = 36
prime = []
for i in range(2, b+1):
    c = 0
    for j in range(2, i//2+1):
        if i % j == 0:
            c = 1
            break
    if c == 0:
        prime.append(i)
print(prime)
i = 0
fact = 1
while b not in prime:
    if b % prime[i] == 0:
        b = b // prime[i]
        fact = fact * prime[i]
    else:
        i = i + 1
print(fact * b)


n = int(input("Enter N: "))
while n >= 1:
    if n % 2 == 0:
        print(n)
    n = n - 1

n = int(input("Enter N: "))
sum = 0
for i in range(1, n*2, 2):
    sum = sum + i
print("Sum =", sum)

n = int(input("Enter N: "))
c = 1
for i in range(n):
    for j in range(n):
        print(str(c).zfill(2),end=" ")
        c+=1
    print()

n = input("Enter the number: ")
l=len(n)
arm=0
for i in n:
    arm+=int(i)**l
print("Armstrong number" if int(n)==arm else "Not Armstrong number")
    






