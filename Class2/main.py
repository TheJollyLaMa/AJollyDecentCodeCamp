"""
Overview
	1.	Type Casting: Converting one data type to another (e.g., str to int, float to int).
	2.	User Input: Using input() to gather user data from the console.
	3.	If Statements: Performing conditional checks and branching logic in your code.


    Section 1: Type Casting

A. Introduction
	•	What is Type Casting?
Type casting (also known as type conversion) is the process of converting data from one type to another, such as:
	•	int("42") -> Converts the string "42" to an integer 42
	•	float("3.14") -> Converts the string "3.14" to a float 3.14
	•	str(99) -> Converts the integer 99 to the string "99"
	•	Why Do We Need It?
When you receive user input in Python, it’s always a string. 
If you need to perform arithmetic operations, you must convert that string to an integer or float first. 
Similarly, sometimes you have integers or floats that need to be turned into strings for printing or concatenation.
"""

# string to int
number_str = "100"
number_int = int(number_str)
print(type(number_int))  # <class 'int'>

# int to float
num = 10
num_float = float(num)
print(num_float)        # 10.0

# int to str
num = 123
text = "Your score is " + str(num)
print(text)             # Your score is 123

"""
C. Practice Exercises (Type Casting)
	1.	Convert Temperature
	•	Ask the user to input a temperature in Celsius (as a string).
	•	Convert it to a float.
	•	Print the Fahrenheit equivalent (F = C * 9/5 + 32).
	2.	Area of a Circle
	•	Prompt the user for a radius (string).
	•	Convert to float.
	•	Calculate the area of the circle (π * r^2).
	•	Print the area (in float).
	3.	Combine Numbers and Text
	•	Prompt the user for a numeric grade (like 95).
	•	Convert it to integer.
	•	Print a message: "Your grade is: X", making sure to convert the integer back to string when you print.
"""
#Add your code here

"""	
•	What is User Input?
In Python, input() is a built-in function that reads a line from standard input (usually the keyboard) and returns it as a string.
	•	Why Use It?
Allows your program to interact with the user—gathering data, preferences, or instructions at runtime.
"""

# name input
name = input("Enter your name: ")
print("Hello, " + name + "!")


# age check
age_str = input("How old are you? ")
age = int(age_str)  # convert string to int
print("Next year, you will be", age + 1)


"""
C. Practice Exercises (User Input)
	1.	Favorite Color
	•	Prompt the user: "What is your favorite color?"
	•	Print a friendly sentence using the color.
	2.	BMI Calculator
	•	Ask the user for their weight (kg) and height (m).
	•	Convert both to floats.
	•	Calculate BMI as weight / (height ** 2).
	•	Print the BMI result.
	3.	Simple Voting Eligibility
	•	Ask the user for their age.
	•	Convert to int.
	•	Print a statement: "You can vote" if age >= 18, otherwise "You cannot vote yet".
"""




"""
•	What is an If Statement?
    An if statement lets you run certain code only if a specified condition is true.
    It’s essential for decision-making in your program. Your code can handle different scenarios differently depending on user input or any other data.
"""

num = 10
if num > 5:
    print("Number is greater than 5")
else:
    print("Number is 5 or less")



grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("D or below")



is_logged_in = True
is_admin = False

if is_logged_in:
    if is_admin:
        print("Welcome, Admin!")
    else:
        print("Welcome, User!")
else:
    print("Please log in first.")


"""
C. Practice Exercises (If Statements)
	1.	Weather Suggestion
	•	Prompt the user to enter the current weather (e.g., rainy, sunny, cold).
	•	Based on the input, suggest an outfit or accessory (umbrella, jacket, etc.).
	•	Use if-elif-else for multiple possibilities.
	2.	Number Comparison
	•	Prompt the user to input two numbers.
	•	Convert both to int or float.
	•	Compare them: print which one is larger or if they are equal.
	3.	Discount Calculator
	•	Prompt the user for a purchase amount (float).
	•	If the amount is above $100, apply a 10% discount. Otherwise, apply no discount.
	•	Print the final price.
	4.	Even/Odd Checker
	•	Prompt the user for an integer.
	•	Check if it’s even or odd using the modulo operator (%).
	•	Print an appropriate message.
"""


import random

def guess_the_number():
    secret_number = random.randint(1, 10)
    attempts_left = 3

    while attempts_left > 0:
        user_guess_str = input(f"You have {attempts_left} attempts. Guess the number (1-10): ")
        
        # Type casting from string to integer
        try:
            user_guess = int(user_guess_str)
        except ValueError:
            print("Please enter a valid number!")
            continue

        if user_guess == secret_number:
            print("Congratulations, you guessed correctly!")
            return
        elif user_guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        attempts_left -= 1

    print(f"Sorry, you are out of attempts. The number was {secret_number}.")

guess_the_number()