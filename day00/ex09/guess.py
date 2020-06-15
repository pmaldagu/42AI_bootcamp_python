import random as rd

if __name__ == "__main__":
    x = 42
    print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n")
    ans = 0
    count = 1
    while ans == 0:
        y = input("What's your guess between 1 and 99?\n>> ")
        if y == "exit":
            print("Goodbye!")
            ans = 1
        elif int(y) == x and x == 42:
            print("The answer to the ultimate question of life, the universe and everything is {}.\nCongratulations! You got it on your first try!".format(y))
            ans = 1
        elif int(y) == x and count == 0:
            print("First try!")
            ans = 1
        elif int(y) != x:
            if int(y) > x and y.isdigit() is True:
                print("Too high!")
            elif y.isdigit() is False:
                print("That's not a number.")
            elif int(y) < x and y.isdigit() is True:
                print("Too low!")
            count += 1
        elif int(y) == x and count > 0:
            print("Congratulations, you've got it!\nYou won in {} attempts!".format(count))
            ans = 1
        elif y == "exit":
            print("Goodbye!")
            ans = 1


