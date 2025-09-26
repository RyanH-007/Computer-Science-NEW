# print("Hello " + input("What is your name? " ) +"!")
# input("Your a beah")
# name = input("What is your name? ")
# print(len(name))

# glass1 = "milk"
# glass2 = "juice"

# glass1 = glass2 


# Band Name generator project:

# # Welcome message
# print("Welcome to the Band Name Generator.")
# # get city name
# city_name = input("What city did you grow up in? \n")

# # get pet name
# pet_name = input("What your pet's name? \n")

# # Combine names

# band_name = city_name + " " + pet_name 

# # Output band name
# print( "Your band name could be " + (band_name))


# print("abcdefg"[-4])

# # Using the type function
# print(type(3.5))
# print(type("5..55"))
# print(type(2))
# print(type(True))


# print("Number of letters in your name: " + str(len(input("Enter your name - "))))



# a = type(234)
# if a == int:
#     print(True)
# else:
#     print(False)


# height = 1.65
# weight = 84 

# bmi = (weight / height**2)

# print(round(bmi))

# # or rounding to two decimal places :
# print(round (bmi,2) )

# my_number = 65.3048576
# print(round(my_number, 4))

# when wanting to add 1 to a variable
# score = 0 
# score = score + 1

# instead do this:

# score = 0 
# score += 1
# print (f"Your score is {score}")


# Tip Calculator 

# print("Welcome to the tip calculator!")
# original_bill = float(input("What was the total bill? - "))
# tip = int(input("How much tip would you like to give? 10%, 12%, or 15%? - "))
# tip = tip / 100

# tip = 1 + tip

# original_bill = original_bill * tip

# people_splitting = int(input("How many people splitting the bill? "))

# bill = round(original_bill / people_splitting, 2 )

# print(f"Each person needs to pay - £{bill}")



# # Testing if number is even

# number = int(input("Give me a whole number > 2 - "))

# number = number % 2

# if number == 0:
#     print("The number you provided is even")
# else: 
#     print("The number you provided is odd")


# # Bmi Calc with a couple conditions

# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)

# if bmi <18.5:
#     print("underweight")
# elif bmi <25:
#     print("normal weight")
# else:
#     print("overweight")



# # Pizza Delivery program

# print("Welcome to Python Pizza Deliveries!")

# size = input("What size pizza do you want? S, M or L: ")
# pepporoni = input("Do you want pepporoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill = 0

# if size == "S":
#     bill += 15
#     if pepporoni == "Y":
#         bill += 2
        
# elif size == "M":
#     bill += 20


    
# elif size == "L":
#     bill += 25
    

# if size != "S":
#     if pepporoni == "Y":
#         bill += 3


# if extra_cheese == "Y":
#     bill += 1

# print(f"Your total is ${bill}")



# Treasure Island Program

# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")

# b_direction = input("Your're at a cross road. Where do you want to go?\n        Type \"left\"  or  \"right\" \n - ").lower()
# if b_direction != "left":
#     print("You fell into a hole. Game Over")
#     exit()

# b_lake_decision = input("You have come to a lake. There is an island in the middle of the lake.\n   Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n - ").lower()
# if b_lake_decision != "wait":
#     print("You were attacked by trout. Game Over")
#     exit()

# s_door_decision = input("You arrive at the island unharmed. There is a house with 3 doors.\n    One red, one yellow and one blue. Which colour do you choose?\n - ").lower()
# if s_door_decision == "yellow":
#     print("You Win!")
# elif s_door_decision == "red":
#     print("You were burned by fire. Game Over")
# elif s_door_decision == "blue":
#     print("You were eaten by beasts. Game Over")
# else:
#     print("Game Over")



# import random 
# a = random.randint(1,10)
# print(a)


# heads or tails program

# import random
# i_random_number_generator = random.randint(1,2)
# if i_random_number_generator == 1:
#     print("Heads")
# else:
#     print("Tails")



# import random 

# names = ["Angela", "Brian", "James", "Clark"]
# rand_gen = random.randint(0,3)
# print(names[rand_gen])



# fruits = ["Strawb", "Melons", "Bluebs"]
# vegetables = ["Spinach", "Kale", "Aubergine"]
# combined = [fruits, vegetables]
# print(combined[1][2])



# Rock paper scissors game

import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

i_user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n- "))

# game_list = ["Rock", "Paper", "Scissors"]

i_computer_choice = random.randint(0,2)





if i_user_choice == 0:
    if i_computer_choice == 2:
        print(f"You chose rock:\n{rock}")
        print(f"The computer chose scissors:\n{scissors}")
        print("You won")
    elif i_computer_choice == 1:
        print(f"You chose rock:\n{rock}")
        print(f"The computer chose paper:\n{paper}")
        print("You loose.")
    elif i_computer_choice == 0:
        print(f"You chose rock:\n{rock}")
        print(f"The computer chose rock:\n{rock}")
        print("Draw")

elif i_user_choice == 1:
    if i_computer_choice == 0:
       print(f"You chose paper:\n{paper}")
       print(f"The computer chose rock:\n{rock}")
       print("You win!")
    elif i_computer_choice == 1:
        print(f"You chose paper:\n{paper}")
        print(f"The computer chose paper:\n{paper}")
        print("Draw")
    elif i_computer_choice == 2:
        print(f"You chose paper:\n{paper}")
        print(f"The computer chose scissors:\n{scissors}")
        print("You loose")

elif i_user_choice == 2:
    if i_computer_choice == 0:
        print(f"You chose scissors:\n{scissors}")
        print(f"The computer chose rock:\n{rock}")
        print("You loose")
    elif i_computer_choice == 1:
        print(f"You chose scissors:\n{scissors}")
        print(f"The computer chose paper:\n{paper}")
        print("You win")
    elif i_computer_choice == 2:
        print(f"You chose scissors:\n{scissors}")
        print(f"The computer chose scissors:\n{scissors}")
        print("Draw")
else:
    print("Please enter again.")

    


