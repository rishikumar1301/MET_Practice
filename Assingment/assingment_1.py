# 1. Ask the user for their full name and print only the first name using slicing and indexing

name = input("Enter Your Full Name")
last_name = name[0:name.find(" "):]
print(last_name)
# output = Enter Your Full Name Rishi kumar
# Rishi

#-------------------------------------------------------------------------------------------------------------------------------------------------------


# 2. Take the user's input for a city name and print it in uppercase, lowercase, and title case
city = input("City name")
print(city.upper())
print(city.lower())
print(city.title())
# output = City name ranchi
# RANCHI
# ranchi
# Ranchi

#---------------------------------------------------------------------------------------------------------------------------------------------
# 3. Print the reversed version of the string 'Technology' using slicing.

str = "Technology"
print(str[::-1])
# output = ygolonhceT


#----------------------------------------------------------------------------------------------------------------------------------------------

# 4. Combine the strings 'Data' and 'Science' with a hyphen and display the resul
word = 'Data','Science'
c = ",".join(word)
print(c)
# output = Data,Science

#----------------------------------------------------------------------------------------------------------------------------------------------

# 5. Ask the user for a product price and display it formatted as currency with two decimal places.
price = input("enter the product price")
print(f"₹{price}.00")
# output = enter the product price 100
# ₹100.00

#----------------------------------------------------------------------------------------------------------------------------------------------

# 6. Store your name and age in variables, then print a sentence using f-string formatting
name = input("Enter your name")
age = input("Enter your age")

print(f"Your name is {name} and age is {age}")
# output = Enter your name rishi
# Enter your age 23
# Your name is rishi and age is 23

#---------------------------------------------------------------------------------------------------------------------------------------------

# 7. Check if the word 'Python' is present in the sentence 'Python is awesome' and print the result.

word = "Python is awesome"
result = word.find("Python")
print(result)
# output = 0

#---------------------------------------------------------------------------------------------------------------------------------------------

# 8. Ask the user for a sentence and display how many characters it contains (excluding leading/trailing spaces).
sentence = input("enter your sentence")

trimed_sentence = sentence.strip()
length = len(trimed_sentence)
print(length)
# output = enter your sentence how are you  
# 11

#---------------------------------------------------------------------------------------------------------------------------------------------

# 9. Use assignment operators to add tax (5%) to a product price of 200 and print the final price.
price = 200
tax =  200*0.05
price += tax

print(price)
# output = 210.0

#---------------------------------------------------------------------------------------------------------------------------------------------

# 10. Given name = 'Alice', print whether the character 'i' is in the name and also if 'z' is not
name = "Alice"
print("i"in name)
print("z" in name)
# output = True
#         False

#---------------------------------------------------------------------------------------------------------------------------------------------

# 11. Use arithmetic operators to calculate and print the average of three user-provided test scores
user1 = int(input("Enter your score"))
user2 = int(input("Enter your score"))
user3 = int(input("Enter your score"))

sum = user1 + user2 + user3

avg = sum/3

print(avg)
# output = Enter your score 10
# Enter your score 20
# Enter your score 30
# 20.0

#-------------------------------------------------------------------------------------------------------------------------------------------

# 12. Ask the user for their height in meters and weight in kilograms, then calculate and print their BMI(Body Mass Index)
height = input("Enter Your height in meter")
weight = input("Enter your weight")

height  **=height 
bmi = weight/height

print(bmi)