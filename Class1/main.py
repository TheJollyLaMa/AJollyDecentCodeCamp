#  1. Print Numbers 1 through 10
#	•	Goal: Practice a basic for or while loop.
#	•	Task: Use a loop to print numbers 1 through 10.

# Example using for:
# for i in range(1, 11):
#     print(i)



# 2. Sum of First N Natural Numbers
# 	•	Goal: Practice accumulating a value in a loop.
# 	•	Task: Write a program that takes an integer N from the user and calculates the sum of numbers from 1 to N.


# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f"{i} x {j} = {i * j}")
#     print()  # Blank line for readability



# 3. Count Down from a Number
# 	•	Goal: Practice while loops and decreasing counters.
# 	•	Task: Prompt the user for a starting number, then use a while loop to count down to zero, printing each number.
# start = int(input("Enter the starting number: "))
# while start >= 0:
#     print(start)
#     print("⸬")
#     start -= 1
# print("💥🤯💥")


# 4. Print Even Numbers in a Range
# 	•	Goal: Filter items in a loop using conditionals.
# 	•	Task: Ask the user for two integers (start and end) and print only the even numbers within this range (inclusive).

# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))

# for i in range(start, end + 1):
#     if i % 2 == 0:
#         print(i)    


# 5. Multiplication Table
	# •	Goal: Nested loops (loop inside another loop).
	# •	Task: Print a multiplication table for the numbers 1 to 5.

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f"{i} x {j} = {i * j}")
#     print()  # Blank line for readability



# 6. Sum of Digits of a Number
# 	•	Goal: Practice loops with arithmetic operations.
# 	•	Task: Prompt the user for a positive integer, and then compute the sum of all its digits.

# num = int(input("Enter a positive integer: "))
# total = 0
# while num > 0:
#     digit = num % 10      # get the last digit
#     total += digit        # add it to the sum
#     num = num // 10       # remove the last digit

# print("Sum of digits:", total)




# 7. Reverse a String
# 	•	Goal: Looping over a string, string indexing, or slicing.
# 	•	Task: Ask the user to enter a string and then print the string in reverse order, character by character.


# text = input("Enter a string: ")

# Method 1: Using a loop
# reversed_text = ""
# for char in text:
#     reversed_text = char + reversed_text
# print("Reversed string:", reversed_text)

# Method 2 (simpler, but still good to demonstrate slicing):
# print("Reversed string:", text[::-1])


# 8. Average of a List of Numbers
# 	•	Goal: Looping over a list and calculating an average.
# 	•	Task: Write a program that takes a list of numbers (e.g., [2, 4, 6, 8]) and computes the average.

# numbers = [2, 4, 6, 8]
# total = 0
# for number in numbers:
#     total += number
# average = total / len(numbers)
# print("Average:", average)



# 9. Print a Simple Pattern (Triangle)
# 	•	Goal: Use loops to create a pattern.
# 	•	Task: Print a triangle of asterisks for a given number of rows.

# rows = int(input("Enter the number of rows: "))

# for i in range(1, rows + 1):
#     print("*" * i)



# 10. FizzBuzz Variation
# 	•	Goal: Common coding challenge that uses loops, conditionals, and modular arithmetic.
# 	•	Task: For numbers from 1 to 20:
# 	•	If the number is divisible by 3, print “Fizz”.
# 	•	If the number is divisible by 5, print “Buzz”.
# 	•	If the number is divisible by both, print “FizzBuzz”.
# 	•	Otherwise, print the number.


# for i in range(1, 21):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)



# Bonus Challenge: Guess the Number Game
# 	1.	Goal: Practice a while loop with conditionals and user input.
# 	2.	Task:
# 	•	The program chooses a random number between 1 and 10.
# 	•	The user attempts to guess the number.
# 	•	If the guess is wrong, prompt the user to guess again until they get it right or run out of attempts.



# import random

# secret_number = random.randint(1, 10)
# attempts = 3

# while attempts > 0:
#     guess = int(input(f"You have {attempts} attempts left. Guess the number (1-10): "))
#     if guess == secret_number:
#         print("Congratulations, you guessed correctly!")
#         break
#     else:
#         print("Wrong guess!")
#         attempts -= 1

# if attempts == 0:
#     print(f"Sorry, you're out of attempts. The secret number was {secret_number}.")