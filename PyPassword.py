from ntpath import join
import random
print("Welcome to the PyPassword Generator!")

nr_of_letters = int(input(f"How manny letters would you like in your password?\n"))
nr_of_numbers = int(input(f"How many symbols would you like?\n"))
nr_of_symbols = int(input(f"How many numbers would you like?\n"))



letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'x','y','z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')']

password = []

for char in range(1, nr_of_letters + 1):
    password.append(random.choice(letters))

for char in range(1, nr_of_numbers + 1):
    password.append(random.choice(numbers))

for char in range(1,nr_of_numbers, +1):
    password.append(random.choice(symbols))

random.shuffle(password)

password_off= ""
for char in password:
    password_off += char

print(f"Your password is: {password_off}")

#You can also youse .join method
