import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')']

password = []
finalpass = ""
print("Welcome to the PyPassword Generator!")
nr_letter = int(input("How many letters would you like in your password?\n"))
nr_symbol = int(input(f"How many symbols would you like?\n"))
nr_number = int(input(f"How many numbers would you like?\n"))

for let in range(nr_letter):
    password.append(random.choice(letters))

for num in range(nr_number):
    password.append(random.choice(numbers))

for sym in range(nr_symbol):
    password.append(random.choice(symbols))

random.shuffle(password)

for things in password:
    finalpass += things

print(f"Your password is: {finalpass}")
