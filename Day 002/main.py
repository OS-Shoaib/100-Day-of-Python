# Day 002
# tip calculator

def tip_calc():
    print("Welcome to the tib calculator.\n")
    total_bil = float(input("What was the total bill? $"))
    people_number = int(input("How many people to split the bill? "))
    per_tip = int(input("what percentage tip would you like to give? "))
    total_amount = total_bil + (total_bil * (per_tip/100))
    person_pay = total_amount / people_number
    # final = round(person_pay, 2)
    final = ":.2f".format(person_pay)
    print("Each person should pay: ${}".format(final))


if __name__ == '__main__':
    x = "y"
    while x == "y":
        tip_calc()
        x = input("Do you want to play again? ")
