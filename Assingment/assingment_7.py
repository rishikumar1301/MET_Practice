# #1. Write a function called greet_user that takes a named argument 'name' and returns 'Hello, {name}!'

# def greet_user(name):
#     return (f"Hello {name}!")

# name = input('Enter the user name :')

# print(greet_user(name))

# # 2. Create a function 'check_temperature' that takes a named argument 'temp' and returns 'Fever' if temp > 99 else 'Normal

# def cheak_temperature(temp):
#     if temp>99:
#         return "Fever"
#     else:
#         return "Normal"
# temp = int(input("Enter the body Temperature: "))

# result = cheak_temperature(temp)

# print(result)

# #3. Define a function 'get_last_fruit' that takes a list of fruits as input and returns the last fruit.

# def get_last_fruit(fruits_list):
#     return fruits_list[-1]

# fruits = ["apple","banana", "kiwi", "pine"]

# last_fruit = get_last_fruit(fruits)

# print(last_fruit)

# # 4. Create a function 'get_price_tag' that takes a 'price' and returns 'Expensive' if price > 1000 else 'Affordable'
# def get_price_tag(rate):
   
#     if rate>1000:
#         return "Expensive"
#     else:
#         return "Affordable"    
# price = int(input("Enter the price : "))

# print(get_price_tag(price))

# # 5. Write a function 'format_user_info' that takes name and age as keyword arguments and returns a formatted string using f-string.

# def formate_user_info(name, age):
#     result = f"Your name is {name} and age is {age}"
#     return result
# name = input("Enter the your name :")
# age = input("Enter the your age : ")

# print(formate_user_info(name, age))

# # 6. Define a function 'uppercase_if_string' that takes one argument and returns it in uppercase if it's a string, else return 'Invalid input'.

# def uppercase_if_string(value):
#     if type(value) == str:
#         return value.upper()
#     else:
#         return "Invalid Input"

# string = int(input("Enter your String: "))
# upper_str = uppercase_if_string(string)
# print(upper_str)


# # 7. Write a function 'safe_divide' that takes two numbers as keyword arguments 'num' and 'den'. Return the result if den is not 0, else return 'Cannot divide
# def safe_divide(num,den):
#     if den != 0:
#         return num/den
#     else:
#         return "Can not divide"

# num1 = int(input("Enter the number : "))
# num2 = int(input("Enter the number : "))
# result = safe_divide(num1,num2)
# print(result)

# # 8. Write a function 'check_login' that takes a dictionary with 'username' and 'password'. Return 'Login successful' if password is not empty

# def check_login(info):
#     if info.get("password"):
#         return "Login successful"
#     else:
#         return "Login Faild" 
# user_credential = {
#     "username": "Rishi",
#     "password": "R123@"
# }

# result = check_login(user_credential)
# print(result)

# # 9. Create a function 'get_full_name' that takes 'first' and 'last' as named arguments and returns full name in title case.

# def get_full_name(f_name, l_name):
#     return f"{f_name} {l_name}".title()
# first= input("Enter the first name: ")
# last= input("Enter the last name: ")
# full_name = get_full_name(first, last)
# print(full_name)    

# # 10. Write a function 'get_discounted_price' that takes 'price' and 'is_member'. If is_member is True, return price * 0.9 else return price

# def get_discount(rate, is_member):
#     if is_member:
#         return rate * 0.9
#     else:
#         return rate
    

# price = 2000
# is_member = True

# discount_price = get_discount(price, is_member)
# print(discount_price)