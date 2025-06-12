# 1. Create a set of your 3 favorite programming languages and print the set.

fav_prg = {"Python", "javascript", "c++"}
print(fav_prg)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 2. Ask the user to enter 3 hobbies separated by spaces. Convert them to a set and print it

hobbies = input("Enter your Hobbies sperated with space")
hobbies_list = hobbies.split()
hobbies_set = set(hobbies_list)
print(hobbies_set)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 3. Create a set called colors with 'red', 'blue', 'green'. Add 'yellow' to it and print the set.
colors = {'red', 'blue', 'green'}
colors.add("yellow")
print(colors)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 4. Given two sets: {'apple', 'banana'} and {'banana', 'cherry'}, update the first set with the second.

#---------------------------------------------------------------------------------------------------------------------------------------------

set1 = {'apple', 'banana'}
set2 = {'banana', 'cherry'}
set1.update(set2)
print(set1)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 5. Create two sets of cities visited by Person A and Person B. Print the union of both.

city1 = {"ranchi","delhi", "mumbai"}
city2 = {"delhi","hyderabad","pune"}
union = city1 | city2
print(union)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 6. Print the intersection of these sets: {'alex', 'john', 'mike'} and {'john', 'mike', 'lisa'}
set1 = {'alex', 'john', 'mike'}
set2 = {'john', 'mike', 'lisa'}
z = set1 & set2
print(z)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 7. Create a set with items: 'pen', 'pencil', 'eraser'. Remove 'pencil' using discard()
items =  {'pen', 'pencil', 'eraser'}
items.discard("pencil")
print(items)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 8. Try to remove an item 'marker' from the set using remove() and observe what happens
items =  {'pen', 'pencil', 'eraser'}
items.remove('marker')
print(items)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 9. Use pop() on a set of weekdays and print the element removed and the updated set.
weekdays = {"monday","tuesday", "wednesday", "thrusday","friday"}
remv = weekdays.pop()
print(remv)
print(weekdays)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 10. Clear a set of car brands and print it to confirm it is empty.
cars = {"tata","mahindara","bmw","byd"}
cars.clear()
print(cars)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 11. Delete a set of tools and try to print it afterward. What error do you get?
tools = {"hammer", "screwdriver", "wrench"}
del tools
print(tools)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 12. Create a set from the string 'hello' and print it
letters_set = set('hello')
print(letters_set)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 13. Ask the user to enter five words, split them, convert to set, and print unique words
words = input("Enter any words")
words_list = words.split()
words_set = set(words_list)
print(words_set)

#---------------------------------------------------------------------------------------------------------------------------------------------

#14. Given sets A = {'a', 'b', 'c'} and B = {'c', 'd', 'e'}, print elements unique to A (difference).
A = {'a', 'b', 'c'}
B = {'c', 'd', 'e'}
c = A - B
print(c)

#---------------------------------------------------------------------------------------------------------------------------------------------

# 15. Make a set of items in your room. Add an item to it, then print the number of items in the set
room_items = {"bed", "table", "chair", "lamp"}
room_items.add("mirror")
print(len(room_items))