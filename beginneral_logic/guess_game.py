def main():
    secret = 8
    chance = 0
    limit = 3

    while chance < limit:
        guess = int(input("Guess a number between 1 and 100 : "))
        chance = chance + 1
        if guess == secret:
            print("the secret number is ", secret)
            print("You guessed right!")
            break
        else:
            print("You guessed wrong.")
    else:
        print("Sorry, you ran out of tries.")


if __name__ == '__main__':
    main()
