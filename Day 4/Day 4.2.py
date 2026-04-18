Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> name = input("Enter your full name: ")
Enter your full name: Yenigalla Bhavana
>>> print(name)
Yenigalla Bhavana
>>> quantity = int(input("Enter the number of items: "))
Enter the number of items: 26
>>> print(quantity)
26
>>> price = float(input("Enter the product price: "))
Enter the product price: 299.99
>>> print(price)
299.99
>>> names = input("Enter employee names (space-separated):").split()
Enter employee names (space-separated):Ankit Sharma Ravi
>>> print(names)
['Ankit', 'Sharma', 'Ravi']
>>> tags = input("Enter tags (comma-separated): ").split(',')
Enter tags (comma-separated): sale.discount,new
>>> print(tags)
['sale.discount', 'new']
>>> 
>>> tags = input("Enter tags (comma-separated): ").split(',')
Enter tags (comma-separated): sale,discount,new
>>> print(tags)
['sale', 'discount', 'new']
>>> marks = list(map(int, input("Enter marks: ").split()))
Enter marks: 89 76 94 82
>>> print(marks)
[89, 76, 94, 82]
>>> weights = list(map(float, input("Enter weights: ").split()))
Enter weights: 55.6 62.1 70.3
>>> print(weights)
[55.6, 62.1, 70.3]
>>> dimensions = tuple(map(int, input("Enter length, width,height: ").split()))
Enter length, width,height: 10 20 15
>>> print(dimensions)
(10, 20, 15)
selected_ids = set(map(int, input("Enter selected image IDs:").split()))
Enter selected image IDs:101 102 103 101 104
print(selected_ids)
{104, 101, 102, 103}
profile = eval(input("Enter user profile as a dictionary: "))
Enter user profile as a dictionary: {'name': 'bhavana', 'age': '21', 'role': 'admin'}
print(profile)
{'name': 'bhavana', 'age': '21', 'role': 'admin'}
username, password = input("Enter username and password:").split()
Enter username and password:user01 mypassword123
print("Username:", username)
Username: user01
print("Password:", password)
Password: mypassword123


print("Hello, World!")
Hello, World!
name = "Alice"
age = 25
print("Name:", name, "Age:", age)
SyntaxError: multiple statements found while compiling a single statement
name = "Alice"
age = 25
print("Name:", name, "Age:", age)
Name: Alice Age: 25
print("2024", "02", "07", sep="-")
2024-02-07
print("Hello,", end=" ")
Hello, 
print("World!")
World!
print("Line 1\nLine 2")
Line 1
Line 2
print("Name:\tAlice")
Name:	Alice
name = "Alice"
age = 25
score = 95.5
print("Name:", name, "Age:", age, "Score:", score)
Name: Alice Age: 25 Score: 95.5
KeyboardInterrupt
name = "Bob"
age = 30
score = 88.75
print("Name: %s | Age: %d | Score: %.2f" % (name, age, score))
Name: Bob | Age: 30 | Score: 88.75
name = "Charlie"
age = 28
score = 92.389
print(f"Name: {name} | Age: {age} | Score: {score:.2f}")
Name: Charlie | Age: 28 | Score: 92.39
name = "Diana"
age = 22
score = 89.456
print("Name: {} | Age: {} | Score: {:.1f}".format(name, age,score))
Name: Diana | Age: 22 | Score: 89.5
