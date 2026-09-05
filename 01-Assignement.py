# Question 1 — Variables + print()

# What will this Python code output?

name = "Khoshal"
age = 18

print(name)
print(age)
print("My name is", name, "and I am", age)

# Your task: Tell me exactly what you think the three output lines will be.
# Answer:
# My name is Khoshal and I am 18


# Question 2 — Data Types
# What will this print?

x = 10
y = 10.5
z = "10"

print(type(x))
print(type(y))
print(type(z))

# Tell me the three outputs.
# int, float, str


# Question 3 — Casting
# What will this code output?

x = "25"
y = int(x)

print(y)
print(type(y))

# 25
# int


# Question 4 — Numbers & Operators
# What will this code print?

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# 13
# 7
# 30
# 3.333


# Question 5 — Casting Challenge 🧠
# What will this code output?

x = 5
y = "10"

print(x + int(y))  # 15
print(str(x) + y)  # 510


# Question 6 — Variable Naming 🧠
# Which of these variable names are valid in Python?

# 1name = "Ali"  # not valid
# my_name = "Ali" # valid
# my-name = "Ali" # not valid
# myName = "Ali" # valid
# class = "Python"  # not valid bcz python keyword


# Question 7 — Multiple Assignment
# What will this code output?

x, y, z = 10, 20, 30

print(x) # 10  
print(y) # 20
print(z) # 30


# Question 8 — Changing Variable Values 🔄
# What will this output?

x = 10
x = 20

print(x)  # 20 bcz the first one is not updated by the second one



# Question 9 — String + Number 🧠
# What happens when you run this?

age = 18

print("I am ", age , " years old")
# print("I am " + age + " years old") # The + operator is trying to concatenate a string with an integer, which Python doesn't allow.


# Will it:
# A) Print I am 18 years old  
# B) Give an error
# C) Convert age automatically to a string
# Choose one and explain why.

# I am 18 years old


# Question 10 — Final Challenge for this section 🧠🔥
# Without running the code, what will be the output?

x = "100"
y = 20

x = int(x)
y = str(y)

#print(x + y) # error


# some harder questions


# Question 11 — Boolean + Data Types
# What will this code print?

x = 10
y = 10.0
z = "10"

print(x == y)  # true (because Python compares their numeric values here.)
print(x == z) # false  (because one is an integer and the other is a string.)
print(type(x)) # int
print(type(y)) # float
print(type(z)) # str

# Give me the five outputs and briefly explain why x == y and x == z are different.


# Question 12 — Casting Challenge
# What will each line output?

a = 10
b = 5.5
c = "20"

print(float(a))  # 10.0
print(int(b))  # 5
print(float(c)) # 20.0


# Question 13 — User Input + Casting
# What will happen when this code runs?

name = input("Enter your name: ")
age = input("Enter your age: ")

print(type(name))
print(type(age))


# Question 14 — Practical Mini Problem 💻
# Write Python code that:

# Asks the user for their name
# Asks the user for their age
# Converts the age to an integer
# Prints something like:
# Hello Ali, you are 18 years old.

# Write the code yourself. Don't worry about making it perfect on the first try.

userName = input("What is your good name: ")
userAge = int(input("Enter your age: "))

print("Hello", userName , "you are", userAge , "years old.")