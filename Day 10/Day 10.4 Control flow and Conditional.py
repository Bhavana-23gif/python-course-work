a = int(input("Enter side1: "))
b = int(input("Enter side2: "))
c = int(input("Enter side3: "))
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

ch = input("Enter a character: ")
if ch in "aeiouAEIOU":
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")

h = float(input("Enter height in meters: "))
w = float(input("Enter weight in kg: "))
bmi = w / (h * h)
print("BMI =", bmi)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 25:
    print("Normal")
else:
    print("Overweight")

units = int(input("Enter units used: "))
if units <= 100:
    bill = units * 1
elif units <= 200:
    bill = 100*1 + (units-100)*2
else:
    bill = 100*1 + 100*2 + (units-200)*3
print("Electricity Bill = ₹", bill)

n = int(input("Enter a 3-digit number: "))

a = n // 100
b = (n // 10) % 10
c = n % 10
sum = a**3 + b**3 + c**3
if sum == n:
    print("Armstrong")
else:
    print("Not Armstrong")

pwd = input("Enter password: ")
upper = False
digit = False
special = False
for i in pwd:
    if i.isupper():
        upper = True
    elif i.isdigit():
        digit = True
    elif not i.isalnum():
        special = True
if len(pwd) >= 8 and upper and digit and special:
    print("Strong Password")
else:
    print("Weak Password")

balance = int(input("Enter account balance: "))
withdraw = int(input("Enter withdrawal amount: "))
if withdraw > balance:
    print("Insufficient Balance")
elif withdraw < 500:
    print("Minimum withdrawal is 500")
elif withdraw % 100 != 0:
    print("Amount should be multiple of 100")
else:
    print("Withdrawal Success")

age = int(input("Enter age: "))
fare = 100
if age < 5:
    print("Ticket Fare = ₹0")
elif age < 18:
    print("Ticket Fare = ₹", fare * 0.5)
elif age > 60:
    print("Ticket Fare = ₹", fare * 0.7)
else:
    print("Ticket Fare = ₹100")

time = input("Enter time in HH:MM format: ")
hh = int(time[:2])
mm = time[3:]
if hh == 0:
    print("12:" + mm, "AM")
elif hh < 12:
    print(str(hh) + ":" + mm, "AM")
elif hh == 12:
    print("12:" + mm, "PM")
else:
    print(str(hh-12) + ":" + mm, "PM")

ch = input("Enter a character: ")
a = ord(ch)
if 65 <= a <= 90 or 97 <= a <= 122:
    print("Alphabet")
elif 48 <= a <= 57:
    print("Digit")
else:
    print("Special Symbol")

marks = int(input("Enter marks: "))
if marks >= 90 and marks <= 100:
    print("A")
elif marks >= 85:
    print("B+")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("F")

amt = int(input("Enter amount: "))
a2000 = amt // 2000
amt = amt % 2000
a500 = amt // 500
amt = amt % 500
a200 = amt // 200
amt = amt % 200
a100 = amt // 100
amt = amt % 100
a50 = amt // 50
amt = amt % 50
a20 = amt // 20
amt = amt % 20
a10 = amt // 10
print("2000 notes =", a2000)
print("500 notes =", a500)
print("200 notes =", a200)
print("100 notes =", a100)
print("50 notes =", a50)
print("20 notes =", a20)
print("10 notes =", a10)

day = input("Enter day: ")
age = int(input("Enter age: "))
if day == "Saturday" or day == "Sunday":
    price = 200
else:
    price = 150

if age < 12:
    price = price / 2
print("Ticket Price = ₹", price)

angle = int(input("Enter angle in degrees: "))
if angle < 90:
    print("Acute Angle")
elif angle == 90:
    print("Right Angle")
elif angle < 180:
    print("Obtuse Angle")
elif angle == 180:
    print("Straight Angle")
else:
    print("Invalid Angle")

m1 = int(input("Enter subject1 marks: "))
m2 = int(input("Enter subject2 marks: "))
m3 = int(input("Enter subject3 marks: "))
avg = (m1 + m2 + m3) / 3
if avg > 90 and m1 > 70 and m2 > 70 and m3 > 70:
    print("Admitted")
elif avg > 80:
    print("Waitlisted")
else:
    print("Rejected")

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum = sum + i
if sum == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")

a = int(input("Enter angle1: "))
b = int(input("Enter angle2: "))
c = int(input("Enter angle3: "))
if a+b+c != 180:
    print("Not a Triangle")
elif a == 90 or b == 90 or c == 90:
    print("Right Triangle")
elif a > 90 or b > 90 or c > 90:
    print("Obtuse Triangle")
else:
    print("Acute Triangle")

marks = int(input("Enter marks: "))
if marks >= 91:
    print("GPA = 10")
elif marks >= 81:
    print("GPA = 9")
elif marks >= 71:
    print("GPA = 8")
elif marks >= 61:
    print("GPA = 7")
elif marks >= 51:
    print("GPA = 6")
else:
    print("GPA = 5")

n = int(input("Enter 4-digit number: "))
a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10
if a + b == c + d:
    print("Lucky Number")
else:
    print("Not Lucky")

age = int(input("Enter age: "))
exp = int(input("Enter driving experience: "))
if age < 25 and exp < 3:
    print("High Risk")
elif age > 25 and exp > 5:
    print("Low Risk")
else:
    print("Medium Risk")

age = int(input("Enter age: "))
if age < 12:
    print("Ticket Price = ₹50")
elif age < 60:
    print("Ticket Price = ₹100")
else:
    print("Ticket Price = ₹60")

n = int(input("Enter a number: "))
if 0 <= n <= 9:
    print("Single Digit")
elif 10 <= n <= 99:
    print("Double Digit")
elif 100 <= n <= 999:
    print("Triple Digit")
else:
    print("More than 3 digits")

time = input("Enter time in HH:MM format: ")
hh = int(time[:2])
mm = int(time[3:])
if 0 <= hh <= 23 and 0 <= mm <= 59:
    print("Valid Time")
else:
    print("Invalid Time")

temp = int(input("Enter temperature: "))
if temp < 10:
    print("Very Cold")
elif temp <= 20:
    print("Cold")
elif temp <= 30:
    print("Warm")
else:
    print("Hot")

usage = float(input("Enter data usage in GB: "))
if usage < 1:
    print("Plan A")
elif usage < 5:
    print("Plan B")
else:
    print("Plan C")

n = int(input("Enter 3-digit number: "))

a = n // 100
b = (n // 10) % 10
c = n % 10
if a == b or b == c or a == c:
    print("Duplicates Present")
else:
    print("Unique Digits")

day = int(input("Enter number (1-7): "))
if day == 1:
    print("Monday - Weekday")
elif day == 2:
    print("Tuesday - Weekday")
elif day == 3:
    print("Wednesday - Weekday")
elif day == 4:
    print("Thursday - Weekday")
elif day == 5:
    print("Friday - Weekday")
elif day == 6:
    print("Saturday - Weekend")
elif day == 7:
    print("Sunday - Weekend")
else:
    print("Invalid Input")

attended = int(input("Enter attended classes: "))
total = int(input("Enter total classes: "))
percent = (attended / total) * 100
print("Attendance =", percent)
if percent > 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")

a = int(input("Enter test1 marks: "))
b = int(input("Enter test2 marks: "))
c = int(input("Enter test3 marks: "))
if a < b < c:
    print("Improving")
elif a > b > c:
    print("Declining")
else:
    print("Fluctuating")

num = input("Enter mobile number: ")
if len(num) == 10 and num[0] in "6789" and num.isdigit():
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")


