
num = int(input("Enter the number: "))
if num >0:
    print("Positive number")
else:
    print("Negative number")

 
num = int(input("Enter the number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

 
num = int(input("Enter the number: "))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")


num = int(input("Enter the number: "))
if num % 3 == 0 and num % 7 == 0:
    print("Divisible by both 3 and 7")
else:
    print("Not divisible by both 3 and 7")


year = int(input("Enter the year: "))
if(year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")


marks = int(input("Enter the marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")


num = int(input("Enter the number: "))
if 100 <= num >= 999:
    print("3-digit number")
else:
    print("Not a 3-digit number")


char = input("Enter a character: ")
if char.lower() in ('a', 'e', 'i', 'o', 'u'):
    print("Vowel")
else:
    print("Consonant")


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a>b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a < b:
    print(f"{a} is smaller")
else:
    print(f"{b} is smaller")


num = int(input("Enter a number: "))
if num == 0:
    print("Number is zero")
else:
    print("Number is not zero")


num = int(input("Enter a number: "))
if num % 10 == 0:
    print("Multiple of 10")
else:
    print("Not a multiple of 10")


age = int(input("Enter the age: "))
if age > 18:
    print("Eligible is vote")
else:
    print("Not eligible to vote")


num = int(input("Enter a number: "))
if 1 <= num <= 100:
    print("In range")
else:
    print("Not in range")


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a == b*b:
    print("It is a square")
else:
    print("It is not a square")


str1 = str(input("Enter a string: "))
str2 = str(input("Enter a string: "))
if str1 == str2:
    print("Strings are equal")
else:
    print("Strings are not equal")


num = int(input("Enter a number: "))
if num > 1:
    if num == 2 or num == 3 or num == 5 or num == 7:
        print("Prime number")
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        print("Not a prime number")
    else:
        print("Prime number")
else:
    print("Not a prime number")


num = int(input("Enter a number: "))
if num > 0 and num % 2 == 0:
    print("Positive and Even number")
else:
    print("Condition not satisfied")


char = input("Enter a character: ")
if char.isupper():
    print("Uppercase letter")
else:
    print("Not a uppercase letter")


temp = int(input("Enter a temperature: "))
if temp > 30:
    print("It's hot")
else:
    print("It's not hot")


num = int(input("Ente a number: "))
if 1000 <= num <= 9999 and num % 2 == 0:
    print("4-digit even number")
else:
    print("Not a 4-digit even number")


char = input("Enter a character: ")
if char.isalpha() and char.lower() not in 'aeiou':
    print("Consonant")
else:
    print("Not a consonant")


num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")
elif num % 2 == 0:
    print("Divisible by 2 only")
elif num % 3 == 0:
    print("Divisible by 3 only")
else:
    print("Not divisible by 2 or 3")


num = int(input("Enter a number: "))
if num < 0 and num % 2 != 0:
    print("Negative and odd number")
else:
    print("Not a negative odd number")


str = str(input("Enter a string: "))
if str[0].lower() in 'aeiou':
    print("Starts with vowel")
else:
    print("Does not start with a vowel")


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a+b>c and a+c>b and b+c>a:
    print("Valid triangle")
else:
    print("Not a valid triangle")


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a>=c and a>=b:
    print(f"{a} is the greatest")
elif b>=a and b>=c:
    print(f"{b} is the greatest")
else:
    print(f"{c} is the greatest")


year = int(input("Enter year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("Century leap year")
    else:
        print("Century year but not leap year")
else:
    print("Not a century year")

ch = input("Enter a character: ")
if ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Not a digit")

num = int(input("Enter number: "))
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if temp == rev:
    print("Palindrome number")
else:
    print("Not palindrome")

a = input("Enter first string: ")
b = input("Enter second string: ")
if len(a) > len(b):
    print("First string is longer")
elif len(b) > len(a):
    print("Second string is longer")
else:
    print("Both are equal")

num = int(input("Enter number: "))
if num >= 50 and num <= 100:
    if num % 5 == 0:
        print("In range and divisible by 5")
    else:
        print("In range but not divisible by 5")
else:
    print("Not in range")

pwd = input("Enter password: ")
if len(pwd) >= 8:
    print("Strong password")
else:
    print("Weak password")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
s = a + b
if s % 2 == 0:
    print("Sum is even")
else:
    print("Sum is odd")

ch = input("Enter character: ")
if not(ch.isalnum()):
    print("Special character")
else:
    print("Not a special character")

temp = int(input("Enter temperature: "))
if temp < 15:
    print("Cold")
elif temp <= 30:
    print("Moderate")
else:
    print("Hot")

num = int(input("Enter number: "))
if num < 10 or num > 50:
    print("Outside the range")
else:
    print("Inside the range")

num = int(input("Enter number: "))
i = 1
found = 0
while i * i <= num:
    if i * i == num:
        found = 1
        break
    i = i + 1
if found == 1:
    print("Perfect square")
else:
    print("Not a perfect square")

age1 = int(input("Enter first age: "))
age2 = int(input("Enter second age: "))
if age1 > age2:
    print("First person is older")
elif age2 > age1:
    print("Second person is older")
else:
    print("Both are same age")

angle = int(input("Enter angle: "))
if angle < 90:
    print("Acute angle")
elif angle == 90:
    print("Right angle")
else:
    print("Obtuse angle")
