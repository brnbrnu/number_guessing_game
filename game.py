from random import randint


def number_guess():
    # the number kept
    num = randint(0, 100)
    # print(num)
    print("------ The Game is Begins ------\n")

    # number of rights taken from the user
    right = int(input("Enter number of rights: "))
    print(f"You have {right} answers in the game.\n")

    # Under the control of the number of rights received from the user,
    # an estimate is taken and directed accordingly.

    def again():
        y_or_n = input("\nDo you want to play again (y/n): ")
        if y_or_n == "y":
            number_guess()
        else:
            print("GOODBYEE")

    while right:  # while right != 0
        guess = int(input("Enter a number between 0 and 100: "))
        if guess < num:
            print(f"ABOVE!!\nYour {guess} is less than the number kept.\n")
        elif guess > num:
            print(f"DOWN!!\nYour {guess} is greater than the number kept.\n")
        else:
            print(f"Congratulations you know :D\nYour guess: {guess} and the number kept: {num}")
            again()
            break

        right -= 1

    else:
        print(f"!!! Your guess is over:(( !!!\nYour right: {right}\nThe number kept: {num}")
        again()


number_guess()