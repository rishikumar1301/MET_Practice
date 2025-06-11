from collections import Counter

# 1. Create a dictionary of your 3 favorite foods with their prices and print the dictionary.
# fav_food = {
#     "samosa": 10,
#     "biryani": 100,
#     "fish": 60,   
# }
# print(fav_food)

# # output = {'samosa': 10, 'biryani': 100, 'fish': 60}


#------------------------------------------------------------------------------------------------------------------------------

# # 2. Ask the user to enter 3 subjects and their marks separated by spaces. Create a dictionary and print it.

# score = {}
# input = input("Enter your 3 Subject and Marks sperated by Space\n").split()

# score_card = {
#     input[0]: input[1],
#     input[2]: input[3],
#     input[4]: input[5]   
# }

# print(score_card)
# # output = Enter your 3 Subject and Marks sperated by Space
# # eng 88 maths 84 sst 90
# # {'eng': '88', 'maths': '84', 'sst': '90'}


#------------------------------------------------------------------------------------------------------------------------------

# 3. Create a dictionary called student with keys ‘name’, ‘age’, ‘grade’. Add a new key ‘city’ and print the dictionary

# student = {
#     'name' : "Rishi",
#     'age': 23,
#     'grade':"A"

# }
# student.update({"city":"Ranchi"})
# print(student)
# # output = {'name': 'Rishi', 'age': 23, 'grade': 'A', 'city': 'Ranchi'}


#------------------------------------------------------------------------------------------------------------------------------

# # 4. Given a dictionary {‘a’: 1, ‘b’: 2}, update it with another dictionary {‘b’: 3, ‘c’: 4}. Print the result.

# dict = {
#     "a": 1,
#     "b": 2
# }
# dict2 = {
#     "b": 3,
#     "c": 4,
# }

# dict.update(dict2)
# print(dict)
# # output = {'a': 1, 'b': 3, 'c': 4}


#------------------------------------------------------------------------------------------------------------------------------

# 5. Create two dictionaries for Person A’s skills and Person B’s skills. Merge them and print the combined dictionary
# person_a_skill = {
#     "c++" : "intermideate",
#     "java": "Beginer"
# }
# person_b_skills = {
#     "HTML": "Advanced",
#     "CSS": "Intermediate"
#     }
# merged_skill = {**person_a_skill,**person_b_skills}

# print(merged_skill)
# # output = {'c++': 'intermideate', 'java': 'Beginer', 'HTML': 'Advanced', 'CSS': 'Intermediate'}


#------------------------------------------------------------------------------------------------------------------------------

# 6. Print all keys from this dictionary: {‘apple’: 5, ‘banana’: 3, ‘orange’: 8}.

# no_fruits = {
#     "apple": 5,
#     "banana":3,
#     "orange":8,
# }

# print(no_fruits.keys())
# # output = dict_keys(['apple', 'banana', 'orange'])


#------------------------------------------------------------------------------------------------------------------------------

# 7. Print all values from this dictionary: {‘red’: ‘#FF0000’, ‘green’: ‘#00FF00’, ‘blue’: ‘#0000FF’}.

# color_code = {
#     "red":"#FF0000",
#     "green":"#00FF00",
#     "blue":"#0000FF",
# }

# print(color_code.values())
# # output= dict_values(['#FF0000', '#00FF00', '#0000FF'])


#------------------------------------------------------------------------------------------------------------------------------

# 8. Create a dictionary with items: {‘pen’: 2, ‘pencil’: 5, ‘eraser’: 1}. Remove ‘pencil’ using pop() and print both the removed value and updated dictionary
 
# items =  {"pen": 2,
#           "pencil": 5, 
#           "eraser": 1
#           }
# removed_item = items.pop("pencil")

# print(f"removed item pencil : {removed_item}")
# print(items)
# # output = removed item pencil : 5
#         # {'pen': 2, 'eraser': 1}

#------------------------------------------------------------------------------------------------------------------------------

# 9. Try to access a key ‘marker’ that doesn’t exist in the dictionary using get() method. Print the result

# student = {
#     'name' : "Rishi",
#     'age': 23,
#     'grade':"A"

# }

# print(student.get("marks"))

# # output = None

#------------------------------------------------------------------------------------------------------------------------------

# 10. Create a dictionary of car models and their years. Use popitem() to remove the last item and print what was removed.

# car_models = {
#     "Toyota Corolla": 2018, 
#     "Honda Civic": 2020, 
#     "Ford Mustang": 2022, 
#     "Tesla Model 3": 2023
#     }

# removed_item = car_models.popitem()

# print(f"Pop item : {removed_item}")
# # output = Pop item : ('Tesla Model 3', 2023)


#------------------------------------------------------------------------------------------------------------------------------

# 11. Clear a dictionary of book titles and print it to confirm it is empt

# book_titles = {
#     "1984": "George Orwell", 
#     "To Kill a Mockingbird": "Harper Lee", 
#     "Pride and Prejudice": "Jane Austen"
#     }
# book_titles.clear()
# print("Book title Dictionary after Clear :", book_titles)

# # output = Book title Dictionary after Clear : {}

#------------------------------------------------------------------------------------------------------------------------------

# 12. Delete a dictionary of tools using del and try to print it afterward. What error do you get?

# book_titles = {
#     "1984": "George Orwell", 
#     "To Kill a Mockingbird": "Harper Lee", 
#     "Pride and Prejudice": "Jane Austen"
#     }
# del book_titles

# print(book_titles)
# # output =   print(book_titles) ^^^^^^^^^^^ NameError: name 'book_titles' is not defined


#------------------------------------------------------------------------------------------------------------------------------

# 13. Create a dictionary from two lists: [‘name’, ‘age’, ‘city’] and [‘John’, 25, ‘NYC’] using zip()/

# keys = ["name", "age", "city"]
# values = ["john", 25, "NYC"]

# my_dict = dict(zip(keys, values))
# print(my_dict) 
# # output = {'name': 'john', 'age': 25, 'city': 'NYC'}

#------------------------------------------------------------------------------------------------------------------------------

# 14. Ask the user to enter 5 words. Count the frequency of each word and store in a dictionary.

# words = input("Enter the five words : ").split()
# word_count =dict(Counter(words))
# print(Counter(words))
# # output = Enter the five words :  apple mango apple banana mango
# # {'apple': 2, 'mango': 2, 'banana': 1}


#------------------------------------------------------------------------------------------------------------------------------

# # 15. Given a dictionary {‘x’: 10, ‘y’: 20, ‘z’: 30}, print only the items where the value is greater than 15 using items()




# TODO






#------------------------------------------------------------------------------------------------------------------------------

# 16. Create a dictionary of your favorite movies and their release years. Print the number of movies in the dictionary using len().

# favorite_movies = {
#     'Inception': 2010,
#     'Interstellar': 2014,
#     'The Dark Knight': 2008,
#     'Avengers: Endgame': 2019,
#     '3 Idiots': 2009
# }

# lenth = len(favorite_movies)
# print(lenth)
# # output = 5

#------------------------------------------------------------------------------------------------------------------------------

# 17. Check if the key ‘python’ exists in the dictionary {‘java’: 1995, ‘python’: 1991, ‘c++’: 1985}.

# release_year = {
#     "java": 1995,
#     "python": 1991,
#     "C++": 1985,
# }

# print("python" in release_year)
# # output = True


#------------------------------------------------------------------------------------------------------------------------------
# 18. Create a nested dictionary for a student with personal info and grades. Print the student’s math grade.

# student = {
#     "persional_info": {
#         "name": "Rishi",
#         "Age" : 23,
#         "add": "hyd",
#     },

#     "grades": {
#         "maths": 85,
#         "eng": 87,
#         "phy": 78,
#     },
# }

# math_score = (student.get("grades")).get("maths")

# print("Maths score in nested dictionary : ",math_score)
# # output = Maths score in nested dictionary :  85


#------------------------------------------------------------------------------------------------------------------------------
# 19. Create a dictionary from the string ‘hello’ where keys are characters and values are their ASCII value


# TODO




#------------------------------------------------------------------------------------------------------------------------------

#  20. Make a copy of a dictionary using copy() method. Modify the copy and print both dictionaries to show they’re different

# persional_info = {
#         "name": "Rishi",
#         "Age" : 23,
#         "add": "hyd",
#     }

# persional_info2 = persional_info.copy()

# persional_info2["Age"] = 35

# print(persional_info)
# print(persional_info2)

# # output = {'name': 'Rishi', 'Age': 23, 'add': 'hyd'}
# # {'name': 'Rishi', 'Age': 35, 'add': 'hyd'}