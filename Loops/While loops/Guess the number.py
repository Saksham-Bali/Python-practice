import random
n = int(input("What should be the upper limit for the range of natural number chosen?: "))
x = random.randint(1, n)
guess = 0
while x != guess:
    guess = int(input("Guess a number from the given range: "))
    if guess > x:
        print("Your guess is greater than the number.")
    elif guess < x:
        print("Your guess is lesser than the number.")
    else:
        print("You guessed it correctly.")
print("The number was:", x)
