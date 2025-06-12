# 1. Given fruits = [['jack', 'apple'], ['orange', 'kiwi'], ['dragon', 'grape']], print the first fruit of the last pair.

fruits = [['jack', 'apple'], ['orange', 'kiwi'], ['dragon', 'grape']]

print(fruits[2][0])

# output =dragon

#  2. Create a tuple of coordinates: ((0, 1), (2, 3), (4, 5)). Print the second number in the last  coordinate

coordinate = ((0, 1), (2, 3), (4, 5))

print(coordinate[2][1])
# # output = 5


#  3. You have a list of students: [('Alice', 23), ('Bob', 21)]. Print Bob's age.

student = [('Alice', 23), ('Bob', 21)]

print("Bob's :", student[1][1])
# output = Bob's : 21

#  4. Create a tuple that contains two lists: ([10, 20], [30, 40]). Print the last number.

tuple_list = ([10, 20], [30, 40])

print("last number : ",tuple_list[1][1])
# # output = last number :  40


#  5. Define a list of dictionaries for students with name and age. Print the name of the first student.

student = [
    {
        "name": "Rishav",
        "age": 25,
    },
    {
        "name": "Alex",
        "age": 20,
    }
]
print("Name of the first studen is : ",student[0]["name"])
# output = Name of the first studen is :  Rishav

#  6. Create a dictionary called subject_marks with subject names as keys and list of marks as values. Print the second mark for Math.
subject_marks = {
    "Math": [85, 90, 78],
    "Science": [88, 92, 80],
    "English": [75, 85, 82]
}

print(subject_marks["Math"][1]) 
 # Output: 90


#  7. Define a dictionary inside a dictionary for a user profile. Print the full profile for 'alice'

user = {
    "user1": {
     'name': "alice",
     "age": 30
    }
}

print(user.get("user1").get('name'))

#  8. You have a list called billing_history with dictionaries for each transaction. Print the status of the  second transaction.
billing_history = [
    {
        "transaction_id": 1,
        "amount": 100, 
        "status": "Completed"
    },
    {
        "transaction_id": 2, 
        "amount": 200, 
        "status": "Pending"
    },
    {
        "transaction_id": 3, 
        "amount": 150, 
        "status": "Failed"
    }
]
print(billing_history[1]["status"])

#  9. Create a tuple containing two billing dictionaries. Print the amount from the first transaction.

billing_history = (
    {
        "transaction_id": 2, 
        "amount": 200, 
        "status": "Pending"
    },
    {
        "transaction_id": 3, 
        "amount": 150, 
        "status": "Failed"
    },
)

print(billing_history[0]["amount"])

# 10. Define a list of 3 tuples, each with a city name and a temperature. Print the temperature of the last city.

city_temp = [("hyderabad","28°C "),("Ranchi","30°C"),("Delhi", "36°C")]

print(city_temp[2][1])

# 11. Given a dictionary with user names as keys and list of scores as values, print the last score of a user

score_card ={
    "Chetaniya": [20, 30, 80, 90],
    "Rishi": [98, 70, 80, 60],
    "Kalu": [59, 69, 50, 10]
}

print(score_card["Chetaniya"][-1])

# 12. Make a list of two dictionaries: each dictionary should have keys 'product' and 'price'. Print the product name from the second dictionary
product_detail = [
    {
         "product": "laptop",
         "price": "₹56999"
    },
    {
         "product": "mobile",
         "price": "₹15999"

    }]

print(product_detail[1]["product"])

# 13. Create a list of tuples where each tuple contains (subject, [marks]). Print the second mark for any subject.

subjects_marks = [
    ("Math", [85, 90, 78]),
    ("Science", [88, 76, 92]),
    ("English", [80, 89, 85])
]
print(subjects_marks[1][1][2])

#  14. Define a dictionary with days of the week as keys and a tuple of 2 tasks as values. Print the first task of Monday.

weekly_tasks = {
    "Monday": ("Complete Python project", "Attend team meeting"),
    "Tuesday": ("Review code submissions", "Write documentation"),
    "Wednesday": ("Plan sprint goals", "Fix reported bugs"),
    "Thursday": ("Update database records", "Optimize performance"),
    "Friday": ("Push final updates", "Prepare presentation")
}
print(weekly_tasks["Monday"][1])

#  15. Create a list of dictionaries, where each dictionary contains a student's name and another dictionary with subjects and marks. Print Math marks for the first student

students_data = [
    {"name": "Amit", "marks": {"Math": 88, "Science": 92, "English": 85}},
    {"name": "Priya", "marks": {"Math": 79, "Science": 87, "English": 90}},
    {"name": "Rahul", "marks": {"Math": 95, "Science": 89, "English": 88}}
]
print(students_data[0]["marks"]["Math"])