import math



#BEGINNER COURSE 1:

# print("Hello World") # print the string hello world

# age = 6 # set variable age to 6
# age = 42 # change variable to 42
# print(age) # print variable age

# price = 14.6 # float variable
# first_name = "Michael" # string variable
# is_online = True  # boolean variable

# something = input("Input something: ") # set variable something to input
# print("this is something: " + something) # print variable something

# number = input("Enter a number: ") # set number to input !will be a string!
# opposite_number = 0 - int(number) # convert variable number to int and subtract it from 0 -> set opposite_number to this value
# print("This is the opposite of the number: " + str(opposite_number)) # convert opposite_number back to string to be able to print it with another string

# string = "this is a string" # set a string
# # print(string.capitalize()) # the string is an object with which we can capitalize the first letter using a function for an object by just writing the function after a dot. function is actually a method
# print(string.find("string")) # this will print where in the string we will find the word string. specifically it will start with 0 and count until it finds the first character of the word string so 10 int this case
# print("this" in string) # this is similar but will only say if it found it and output as boolean. whereas the one above will say where and when nowwhere is found will say -1

# print(10 + 3 - 2 * 5, 2 ** 8) # math as usual
# print(11 / 2) # division to float
# print(11 % 2) # division but only what is left so 0 when works and otherwise whats left
# print(11 // 2) # division to integer rounded down, so the rest can always be gotten from operator above

# x = 10 # set var to 10
# x = x + 3 # add 3
# x += 3 # add 3 but more simple

# x = (10 + 3) * 2 # more normal math
# print(x) # print x

# x = 3 > 2 # boolean expressian of true
# x = 3 == 2 # boolean expressian of false
# #some operators: >, <, ==, !=, <=, >=
# print(x) # print x again

# price = 25
# print(price > 10 and price < 30) # both things must be true
# print(price > 50 or price < 20) # 1 or more needs to be true
# print(not price > 50) # not just reverses so false becomes true

# temp = 35 # set temps to 35
# if temp > 10: # if temp higher then 10 run code block
#     print("temp higher than 10") # print
# elif temp > 0: # will not run even though true because it is elif(else if) and not (and if/ or if)
#     print("higher than 0")
# print("done") # will always run

# number = 1
# while number < 16: # repeat until number is not smaller than 16
#     print(number * "*") # will print * however many times as number is in the itteration
#     number += 1 # add 1

# names = ["michi", "malik", "fritzli"]
# print(names[0]) # prints first name in list
# print(names[-1]) # prints last name in list
# print(names[-2]) # prints second last name in list

# names[0] = "michael" # change first element in list to michael
# print(names[0:2]) # prints first 2 names

# num = [1, 3, 5, 7, 88, 10] # make list
# num.append(6) # add 6 as last item in list
# num.insert(1, "hello this isnt a number") # use ctrl + shift + space for help, adds string as secoond item moving rest forward
# num.remove(88) # removes number 88 from list
# num.pop(1) # removes the second item !not number 2 as in .remove!
# #num.clear() # clears list
# print(1 in num) # checks if 1 is in num and outputs boolean True
# print(len(num)) # prints number of elements

# nnum = [1, 4, 7, 10, 13, 304]
# for item in nnum: # for loop using item variable and repeating for every item in list
#     print(item) # same is possible with while but is worse

# rng= range(5)
# print(rng) # prints range(0, 5) instead of how one would expect 12345

# for i in rng: # repeat for every item in rnf so 5 times
#     print(i) # how to properly do it

# for i in range(5, 10, 2): # range from 5 to 9 but only every second item
#     print(i)

# num = (1, 2, 3, 6, 6) # this creates a tuple. tuple = immutable(not modifiable) list
# print(num.count(6)) # will print amount of 6 in tuple
# print(num.index(6)) # will print index of first occurence of this number. print(num.__class__) with underscore its called a magic method(complicated shit)




#TUTORIAL 2

# # class Point: #pascal naming convention for classes by capitalizing first letter of every word
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")

# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()
# point2.x = 1
# print(point2.x)

# first = "michi"
# last = "meier"
# message = first + " [" + last + "] is a coder" # more complex
# print(message)

# msg = f"{first} [{last}] is a coder" # formated string with f infront makes it easier to read in code
# print(msg)

# x = 2.50
# y = -23.4
# print(round(x)) # will round down when exactly in middle ?weird?
# print(abs(y)) # will turn number positive

# print(math.floor(2.7)) # floor of 2.7 is 2 (basically just rounding down)

