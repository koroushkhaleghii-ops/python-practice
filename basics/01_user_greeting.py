"""
Exercise 1: User Greeting
Get name, age, and city from user and print a welcome message.
"""

def get_user_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    
    print("Hello " + name + "! You are " + age + " years old and live in " + city + ".")

get_user_info()