'''
Syntax
------------
if condition :
    #stmts
'''
charger = int(input("Enter the charging: "))
if charger <= 20:
    print("Charge the phone or turn on power saving mode")


products = {
    1:{'name':'bread','discount':10},
    2:{'name':'sugar','discount':0},
    3:{'name':'jam','discount':5},
    4:{'name':'butter','discount':0}
    }
print(products)
index = int(input("Enter the index: "))
if products[index]['discount']:
    print(f'{products[index]["name"]} has discount')


products = {
    1:{'name':'books','bestseller':True},
    2:{'name':'pens','bestseller':False},
    3:{'name':'pencils','bestseller':True},
    4:{'name':'files','bestseller':True}
    }
print(products)
index = int(input("Enter the index: "))
if products[index]['bestseller']:
    print(f'{products[index]["name"]} has bestseller')


'''if else condition--------'''

jd = {'python','mysql','javascript','flask'}
skills = set(input("Enter the skills: ").split())
if jd == skills:
    print("Congrats!! Your resume is shortlisted")
else :
    print(f"Sorry, try again. You need this skills set: {jd-skills}")


plan = False
if plan:
    print("Ads won't run. You can watch the video without interuption")
else:
    print("Ads will run. Subscribe to youtube premium")


time = float(input("Enter the time: "))
if time>=9.00:
    print("You can start your exam")
else :
    print("Wait some more time")



''' if elif else condition----------------'''

wheels = int(input("Enter the wheels: "))
if wheels == 2:
    print("your bike is on the way. Please pay $50")
elif wheels == 3:
    print("Your auto is on the way. Please pay $120")
elif wheels == 4:
    print("Your cab is on the way. Please pay $200")
else :
    print("Enter the valid input")



''' nested if condition-------------------------'''

status = input("Enter the status: ")
if status=='face':
          print("Unlock the mobile")
else :
    print("Unable to reg face")
    if status=='password':
        print("Unlock the mobile")
    else:
        print("Incorrect password")


products = {
    1:{'name':'bread','stock':10},
    2:{'name':'sugar','stock':0},
    3:{'name':'jam','stock':5},
    4:{'name':'butter','stock':0}
    }
login_status = True
print(products)
order_id = int(input("Enter the index to order: "))
if login_status:
    if products[order_id]['stock']:
        print(f"{products[order_id]['name']} is ordered")
    else:
        print(f"{products[order_id]['name']} is out of stock, we will notify you")
else:
    print("Please login to proceed with the order")
    
