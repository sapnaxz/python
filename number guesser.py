# program will generate a random number and count the number of guesses it took for the user to guess it
import random
#r = random.randrange(1, 11) #(start, stop) last number 10

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0 :
        print("Please type a number greater than 0 next time.")
        quit()
else:
        print("Please type a number next time.")
        quit()


random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input ("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number :
        print("You got it, mate! ")
        break

    elif user_guess > random_number: 
        print("You were above the number.")
    else:
        print("You were below the number.")

print("You got it in", guesses, "guesses.") #instead of plus you can use a comma as well