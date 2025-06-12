# 1. Create a list of your 5 favorite fruits and print the first and last fruits.
fruit = ["apple", "banana", "pineapple", "kiwi", "mango"]

print(fruit[0], fruit[4])
# output = apple mango

#--------------------------------------------------------------------------------------------------------------------------------------------

# 2. Ask the user to enter 3 cities they visited recently. Store them in a list and print the list

city1 = input("city1")
city2= input("city2")
city3 = input("city3")
visited_city =[city1, city2, city3]
print(visited_city)

#------------------------------------------------------------------------------------------------------------------------------------------
# 3. From a list of prices [1200, 850, 950, 720], print only the prices above 900 using slicing.

#TODO


#---------------------------------------------------------------------------------------------------------------------------------------------

# 4. Create a list of the first 5 even numbers. Append 12 to it and print the result.
even_num = [2, 4, 6, 8, 10]
even_num.append(12)
print(even_num)


#--------------------------------------------------------------------------------------------------------------------------------------------

# 5. Insert the word 'Python' into the second position of the list ['Java', 'C++', 'Go']and print it
course = ['Java', 'C++', 'Go']
course.insert(1,"Python")
print(course)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 6. Ask the user to input a sentence, then print a list of its words using .split().

sentence = input("Enter any sentence: ")
words = sentence.split()

print(words)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 7. Remove the last item from a list of months ['Jan', 'Feb', 'Mar', 'Apr'] and print the list.
months =  ['Jan', 'Feb', 'Mar', 'Apr']

dlt = months.pop()
print(months)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 8. Copy the list ['car', 'bus', 'train'], sort it, and reverse it. Print the final list.
trv =['car', 'bus', 'train']
trv.sort()
trv.reverse()
print(trv)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 9. Count how many times 'apple' appears in the list ['apple', 'banana', 'apple', 'cherry'].
fruit = ['apple', 'banana', 'apple', 'cherry']
num = fruit.count("apple")
print(num)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 10. Use .format() to print 'Tom has 3 apples and 5 bananas' with variables

apple = 3
banana= 5

print(f"Tom has {apple} apples and {banana} bananas")


#---------------------------------------------------------------------------------------------------------------------------------------------

# 11. Create a list with the characters of the word 'Hello' using list() and print it.

word = list("hello")
print(word)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 12. Create a list of 3 integers. Calculate and print their sum and average.

num = [1, 2, 6]
a = sum(num)
avg = a/len(num)
print(sum(num))
print(avg)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 13. Ask the user for their name and store each character in a list. Print the reversed list

name = input("Enter your name")
char_list  = list(name)
char_list.reverse()
print(char_list)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 14. Given a list of names = ['Alice', 'Bob', 'Charlie'], check if 'Bob' is in the list
names = ['Alice', 'Bob', 'Charlie']

print("Bob" in names)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 15. Clear all elements from a list ['one', 'two', 'three'] and print the list

num = ['one', 'two', 'three']

num.clear()
print(num)