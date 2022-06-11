
# variables: 
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

# if guess is not sercet word and out of gussess becomes true:
while guess != secret_word and  not (out_of_guesses):
    if guess_count < guess_limit: 
        guess = input("Enter guess: ")
        guess_count += 1
    else: 
        out_of_guesses = True

# other way without using not function: 
while guess != secret_word and out_of_guesses != True:
    if guess_count < guess_limit: 
        guess = input("Enter guess: ")
        guess_count += 1
    else: 
        out_of_guesses = True

# other way with one single condition expression and a break statement in order to not have an infinite loop: 
while guess != secret_word:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
        break


# if guess right then out of guesses is true:
if out_of_guesses: 
    print("out of guessses, You lose!")
# if fail the three trys then out of guesses is false:
else: 
    print("You Win!")
