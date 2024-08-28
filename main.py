print("*-----------*ROLLER COASTER*-----------*")
print("*---------*ELIGIBILITY CHECKER*---------*")

height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5")
    elif age<= 18:
        print("Please pay $10")
    else:
        print("Please pay $12")
else:
    print("Sorry..you have to grow taller for the ride!")


