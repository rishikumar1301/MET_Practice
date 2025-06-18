# # 1. Write a function that accepts any number of numbers using *args and returns the sum of all  numbers.
# def sum_args(*args):
#     return sum(args)
# print(sum_args(1,2,3,4))

# # 2. Create a function that accepts any number of keyword arguments (**kwargs) and returns a string of all keys joined by commas.

# def join_keys(**kwargs):
#     ans = ",".join(kwargs.keys())
#     return ans

# print(join_keys(name="Rishi", age=22, country="India"))



# # 3. Write a program that keeps asking for input using input() until the user types 'exit'. Print each input value entered.
# user_intput = ""
# while user_intput!= "exit":
#     user_intput = input("enter your input and for exit enter 'exit'")
#     print(user_intput)



# # 4. Write a while loop that prints numbers starting from 1. Break the loop if the number reaches 5.

# count = 0

# while True:
#     count+=1
#     if count==5:
#         break
#     print(count)


# # 5. Write a while loop that asks the user to enter a number. If the number is negative, use continue to ask again. Stop when a positive number is entered.

# while True:
#     num = int(input("Enter the number"))
#     if num<0:
#         print('you entered negative number please... enter positive number')
#         continue
#     print(f"You enter Positive number :{num}")
#     break



# # 6. Create a function that takes *args and returns the largest value without using max(). Use a while  loop to find the largest.
 
# def largest_num(*nums):
#     n = len(nums)
#     if n<0:
#         return -1
#     i =0
#     max_val = 0
#     while i<n:
#         if nums[i]>max_val:
#             max_val = nums[i]
#         i+= 1
#     return max_val
# result = largest_num(1,2,3,7,5,8)
# print(result)

# # 7. Write a while loop that accepts names using input() and adds them to a list. Stop when the user enters an empty string. Print the list.

# names = []

# while True:
#     name= input("enter the name (leave empty to exit): ")
#     if name == "":
#         break
#     names.append(name)

# print(names)    

# # 8. Write a function that accepts **kwargs containing product names and prices. Return the total price using a while loop

# def total_bill(**product_rate):
#     price_list = list(product_rate.values())
#     i = 0
#     total = 0
#     while i<len(price_list):
#         total+= price_list[i]
#         i+=1
#     return total       
        
# total_price = total_bill(rice=200, apple= 100, laptop=40000, phone= 10700)
# print(total_price)

# # 9. Write a program using while loop that counts down from 10 to 1, but skips number 5 using continue.
# count = 10
# while count>1:
#     if count == 5:
#         count-=1
#         continue

#     print(count)
#     count-=1


# 10. Write a function that asks for user input using input() inside a while loop until a valid age (>0) is entered, then returns the age
def valid_age():

  while True:
    age = int(input("Enter your valid age to exit"))
    if age>0:
     return age
print(valid_age())    