# 1. Write a for loop that prints numbers from 1 to 5 using range().

for x in range(5):
    print(x+1)

# 2. Use a for loop with range() to print all even numbers between 10 and 20.

for x in range(10,20):
    print(x)

# 3. Ask the user for 3 names using input() in a loop. Store them in a list and print the list.

name_list = []
for x in range(3):
    name = input("Enter the name : ")
    name_list.append(name)
print(name_list)   

# 4. Given a list of numbers, use a for loop to print the square of each number
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num**2)   

# 5. Loop through a list of dictionaries with keys 'name' and 'age'. Print each name and age.
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]
for person in people:
    print("Name:", person['name'], ", Age:", person['age'])

# 6. Given a nested list of fruits like [['apple', 'banana'], ['grape', 'mango']], use a for loop to print all fruits. 
fruits = [['apple', 'banana'], ['grape', 'mango']]
for sublist in fruits:
    for fruit in sublist:
        print(fruit)    

# 7. Write a for loop that prints characters of a string entered by the user.
user_input = input("Enter a string: ")
for char in user_input:
    print(char)

# 8. Use range() to print numbers from 5 to 1 in reverse order
for x in range(5,0,-1):
    print(x)

# 9. Write a program that asks the user to input 3 subjects and 3 marks each, then print each subject with its mark.
subjects_marks = {}
for i in range(3):
    subject = input("Enter the subject: ")
    marks = input("Enter the marks: ")
    subjects_marks[subject] = marks

for subject, marks in subjects_marks.items():
    print(f"Subject: {subject}, Marks: {marks}")

# 10. Loop through a list of tuples containing (product, price) and print 'product: price' for each
products = [("apple", 1.2), ("banana", 0.8), ("orange", 1.0)]
for product, price in products:
  print(f"{product}: {price}")
