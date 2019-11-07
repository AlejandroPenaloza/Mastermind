import random
print("                                                          MASTERMIND")
print("                   A random number is generated with the quantity of digits you want.")
print("                   You have to keep inputting the number's digits until you guess the randomly generated number. ")
print("                   After each unsuccessful try the game will indicate you how many numbers you got in the correct")
print("                   position, but not which ones.")
print("                   Every 3 tries the game will ask you if a hint is needed, and it will be printed if wanted")
print("                   At the end, the game will tell you how many tries it took.\n")
print("                                                        ENJOY THE GAME!\n")

keep_playing = True
while keep_playing:
    number_of_digits = input("How many digits do you want to guess?\n")
    while True:
        if number_of_digits.isdigit():
            number_of_digits = int(number_of_digits)
            break
        else:
            print("Try again")
            number_of_digits = input("How many digits do you want to guess?\n")

    counter = 0
    random_digits = []
    for x in range(number_of_digits):
        digit = random.randint(1, 9)
        random_digits.append(digit)

    correct_guessing = False
    while not correct_guessing:
        if counter != 0 and counter % 3 == 0:
            accepted_input = False
            while not accepted_input:
                want_hint = input("Do you want a hint?\n")
                if want_hint == 'yes':
                    random_index = random.randint(0, (number_of_digits - 1))
                    hint = random_digits[random_index]
                    print("One of the right numbers is ", hint, ", in the position ", (random_index + 1))
                    accepted_input = True
                elif want_hint == 'no':
                    accepted_input = True
                else:
                    print("Input not accepted. Type 'yes' or 'no'")
                    accepted_input = False

        right_numbers = []
        for y in range(number_of_digits):
            guess = input("Guess and enter a digit\n")
            if guess.isdigit() == False or len(guess) != 1:
                raise ValueError("Unaccepted input, a digit as input is expected!!!")
            guess = int(guess)
            if guess != random_digits[y]:
                right_numbers.append(0)
            else:
                right_numbers.append(1)
        number_of_corrects = sum(right_numbers)
        if number_of_corrects == number_of_digits:
            correct_guessing = True
            print("Well done! You got all numbers right!")
            print("The number is ", *random_digits, " and it took you ", counter, " try/ies.")
        else:
            correct_guessing = False
            print("Wrong ", number_of_digits, " digits number")
            if number_of_corrects == (number_of_digits - 1):
                print("You are almost there!")
            print("You got ", number_of_corrects, " right digit(s) in its place")
        counter += 1

    answer = input("Do you want to play again!\n")
    if answer == 'yes':
        keep_playing = True
    else:
        print("Game Over")
        keep_playing = False
print(round(cbrt((17/4 + math.sqrt(625/27))/2) + cbrt((   (17/4) - math.sqrt(625/27)  )  /2) + 1/2, 6))
