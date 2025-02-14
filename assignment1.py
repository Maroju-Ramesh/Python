# Conditional Statements and Loops Programs
# Program to check if a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
 print("Positive")
elif num < 0:
 print("Negative")
else:
 print("Zero")
# Program to determine if a number is odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
 print("Even")
else:
 print("Odd")
# Program to check voting eligibility
age = int(input("Enter your age: "))
if age >= 18:
 print("Eligible to vote")
else:
 print("Not eligible to vote")
# Program to find the greatest of two numbers
a, b = map(int, input("Enter two numbers: ").split())
if a > b:
 print("Greatest number:", a)
else:
 print("Greatest number:", b)
# Program to print Pass/Fail based on marks
marks = int(input("Enter marks: "))
if marks > 40:
 print("Pass")
else:
 print("Fail")
# Program to display the day of the week based on a number
day = int(input("Enter a number (1-7): "))
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if 1 <= day <= 7:
 print(days[day-1])
else:
 print("Invalid input")
# Program to implement a simple calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")
if op == '+':
 print("Result:", a + b)
elif op == '-':
 print("Result:", a - b)
elif op == '*':
 print("Result:", a * b)
elif op == '/' and b != 0:
 print("Result:", a / b)
else:
 print("Invalid operation")
# Program to print all numbers from 1 to 100 using a for loop
for i in range(1, 101):
 print(i, end=" ")
# Program to print the sum of the first n natural numbers
n = int(input("Enter n: "))
sum_n = n * (n + 1) // 2
print("Sum:", sum_n)
# Program to print all even numbers between 1 and 50 using a while loop
i = 2
while i <= 50:
 print(i, end=" ")
 i += 2
# Program to display the multiplication table of a number (first 20 terms)
num = int(input("Enter a number: "))
for i in range(1, 21):
 print(f"{num} x {i} = {num * i}")
# Program to reverse a number and sum its digits

num = int(input("Enter a number: "))
rev = 0
sum_digits = 0
while num > 0:
 digit = num % 10
 rev = rev * 10 + digit
 sum_digits += digit
 num //= 10
print("Reversed Number:", rev)
print("Sum of digits:", sum_digits)
# Program to count the number of digits in a given number
num = int(input("Enter a number: "))
count = 0
while num > 0:
 num //= 10
 count += 1
print("Number of digits:", count)
# Program to keep asking for numbers until a negative number is entered
while True:
 num = int(input("Enter a number: "))
 if num < 0:
   break
# Program to print the first 10 terms of Fibonacci series
a, b = 0, 1
for _ in range(10):
 print(a, end=" ")
 a, b = b, a + b
# Program to check if a number is prime
num = int(input("Enter a number: "))
if num > 1:
 for i in range(2, int(num ** 0.5) + 1):
  if num % i == 0:
   print("Not a prime number")
   break
 else:
   print("Prime number")
else:
   print("Not a prime number")
# Program to calculate factorial using a while loop
num = int(input("Enter a number: "))
fact = 1
while num > 1:
 fact *= num
 num -= 1
print("Factorial:", fact)
# Program to print numbers from 1 to 100 divisible by 3 and 5
for i in range(1, 101):
 if i % 3 == 0 and i % 5 == 0:
   print(i, end=" ")
# Menu-driven program to find square or cube
while True:
 print("1. Square a number")
 print("2. Cube a number")
 print("3. Exit")
 choice = int(input("Enter choice: "))
 if choice == 1:
  num = int(input("Enter number: "))
  print("Square:", num ** 2)
 elif choice == 2:
  num = int(input("Enter number: "))
  print("Cube:", num ** 3)
 elif choice == 3:
  break
 else:
  print("Invalid choice")
# Basic login system with 3 attempts
correct_password = "password123"
attempts = 3
while attempts > 0:
 entered_password = input("Enter password: ")
 if entered_password == correct_password:
  print("Access granted")
  break
 else:
  attempts -= 1
  print(f"Incorrect password. {attempts} attempts left.")
if attempts == 0:
 print("Access denied")