# This is the first day project
# Day 001
# Omar Shoaib

def band_gen():
    print("Welcome to the Band Name Generator.\n")
    city_name = input("What's the name of the city you grew up in?\n")
    pet_name = input("what's your pet's name?")
    print("Your band name could be " + city_name + " " + pet_name)


if __name__ == '__main__':
    x = "y"
    while x == "y":
        band_gen()
        x = input("Do you want to play again? ")
