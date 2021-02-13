# Day 005

# Password Generator Project
"""
Book Solution
'I liked it'
# Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
"""

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def pass_gen():
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    return nr_letters, nr_symbols, nr_numbers


def pass_gen_process(nr_letters, nr_symbols, nr_numbers):
    letter_out = ""
    symbol_out = ""
    number_out = ""

    for let in range(nr_letters):
        let = str(random.choice(letters))
        letter_out += let

    for sym in range(nr_symbols):
        sym = str(random.choice(symbols))
        symbol_out += sym

    for num in range(nr_numbers):
        num = str(random.choice(numbers))
        number_out += num

    string_out = letter_out + symbol_out + number_out
    return string_out


def randomization(string_in):
    final_string = ""
    for _ in string_in:
        x = str(random.choice(string_in))
        final_string += x
    print("\nThe new password is: {}".format(final_string))


if __name__ == '__main__':
    letter, symbol, number = pass_gen()
    string = pass_gen_process(letter, symbol, number)
    randomization(string)
