"""Mbulelo Pani, Class 2"""


from default import *

# User enters full names
name = (input("Enter your full names: "))
try:
    age = int(input("Enter your age: ")) # Enters age
except ValueError: # If user incorrectly enters wrong syntax
    print("Please enter enter only your two digit age")
else:
    if age >= 18: # if user is above 18 years, program proceeds
        def play():
            user_numbers = []         # Empty list to be appended is initialised
            for i in range(0,6):        # range for how many numbers the user puts is set
                guess = int(input("Please enter any number between 1 and 49: "))        # input guesses
                # while statement to determine what happens if guess is out of range
                while guess<1 or guess>49:
                    #ask user to try again
                    guess = int(input("Please try again: enter any number between 1 and 49: "))
                user_numbers.append(guess)      # guess is appended to 'user_numbers'
            user_numbers.sort()         # sorts the user's numbers in ascending order

            # create external text file
            file = open('Assignment.txt', 'w+')
            # Results of the program are printed inside the text file
            file.write(str(today))
            file.write("\n")
            file.write("Name: ")
            file.write(name)
            file.write(", ")
            file.write(str(age))
            file.write(" years of age.")
            file.write("\n")
            file.write("Lotto Draw: ")
            file.write(str(Lotto_numbers))
            file.write("\n")
            file.write("Your numbers: ")
            file.write(str(user_numbers))
            file.write("\n")

            count = 0   # this will count correct guess by the user
            for guess in user_numbers:
                if guess in Lotto_numbers:
                    count += 1

            # if statements determine the prize that the user won
            # results printed inside the text file
            if count <= 1:
                file.write("Sorry, better luck next time.")
            elif count == 2:
                file.write("You got " + str(count) + " winning numbers")
                file.write("\n")
                file.write("You only get R20.00")
            elif count == 3:
                file.write("You got " + str(count) + " winning numbers")
                file.write("\n")
                file.write("You have won: R100.50")
            elif count == 4:
                file.write("You got " + str(count) + " winning numbers")
                file.write("\n")
                file.write("You have won: 2 384.00")
            elif count == 5:
                file.write("You got " + str(count) + " winning numbers")
                file.write("\n")
                file.write("You have won: R8 584.00")
            else:
                file.write("You got " + str(count) + " winning numbers")
                file.write("\n")
                file.write("You have won: R10 000 000.00!")
        play()
    else:
        # user who is not above 18 years old cannot play
        print("You have to be the age of 18 or above to play.")
        file = open('Assignment.txt', 'w+')
        file.write("Sorry, you have to be above the age of 18")





