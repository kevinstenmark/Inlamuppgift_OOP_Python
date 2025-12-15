import random

"""
Checking fullname and save into variable player_name
Checks for string to only contain chars, no numerics
Only one whitespace
"""


def get_player_name():
    while True:
        player_name = input("What is your full name?\n")
        # Checking if number is in name
        contains_digit = False
        for chr in player_name:
            if chr.isdigit():
                contains_digit = True
                break
        if contains_digit:
            print("Please try again, name cannot contain numbers")
            continue

        numberOfWhiteSpace = player_name.count(" ")
        if numberOfWhiteSpace == 0:
            print("You must have a space-separator between first and lastname")
            continue
        elif numberOfWhiteSpace > 1:
            print("You can only have one whitespace between first and lastname")
            continue

        parts = player_name.split()
        if len(parts) != 2:
            print("You must provide exatly firstname and lastname")
            continue

        break

    return player_name


"""
Checks player birthdate and validation of:
yyyy > 1900
Checks for months that should only have 30 days
Checks for february and leapyear

"""


def get_player_birthdate():
    while True:
        input_date = input("Input birthdate YYYYMMDD\n")

        if len(input_date) != 8:
            print("Please input birthdate in correct format")
            continue

        year = int(input_date[0:4])
        month = int(input_date[4:6])
        day = int(input_date[6:8])

        if year < 1900:
            print("You cannot be born before 1900")
            continue
        if month < 1 or month > 12:
            print("Birthdate month has to be between 1 and 12")
            continue
        if day < 1 or day > 31:
            print("Birthdate day has to be between 1 and 31")
            continue
        months_with_30_days = [4, 6, 9, 11]
        if month in months_with_30_days:
            if day == 31:
                print("Those months only have 30 days")
                continue
        february_month = 2
        if month == february_month:
            if day == 29:
                if year % 4 != 0:
                    print("Only leapyear for february has 29 days")
                    continue
            elif day > 29:
                print("February only has 28 days if not leap year")
                continue

        player_birthdate = input_date
        return player_birthdate


"""
Calculates player_age from playerbirthday and returns it
"""


def calculate_age(birthdate_string):
    year = birthdate_string[0:4]
    year = int(year)
    current_year = 2022
    player_age = current_year - year
    return player_age


"""
Lucky list of 9 random integers between 0-100
Returns lucky_list
"""


def generate_lucky_list():
    lucky_list = []
    for i in range(9):
        random_number = random.randint(0, 100)
        lucky_list.append(random_number)
    return lucky_list


"""
Generates lucky number, random between 0-100
"""


def generate_lucky_number():
    lucky_number = random.randint(0, 100)
    return lucky_number


"""
Ask to play again function
"""


def ask_to_play_again():
    while True:
        user_play_again = input("Play again? (y/n)\n")
        if user_play_again.startswith("y"):
            return user_play_again
        elif user_play_again.startswith("n"):
            return user_play_again
        else:
            print("Invalid input")


"""
Play round loop
Adds lucky_number to lucky_list
"""


def play_round():
    num_of_tries = 1

    lucky_list = generate_lucky_list()
    lucky_number = generate_lucky_number()

    lucky_list.append(lucky_number)

    print(f"Here is the lucky list! {lucky_list}")
    player_input = int(input("which is the lucky number?"))

    if player_input == lucky_number:
        print(
            f"Congrats, game is over! And you got lucky number from: {num_of_tries} :)"
        )
        answer = ask_to_play_again()
        return answer
    else:
        shorter_list = filter_list(lucky_list, lucky_number)
        while True:
            num_of_tries += 1

            print(f"\nTry number: {num_of_tries}")
            player_input = int(
                input(f"\nNew list is: {shorter_list}, choose the lucky number?")
            )
            if player_input == lucky_number:
                print(
                    f"Congrats, game is over! And you got lucky number from: {num_of_tries} :)"
                )
                answer = ask_to_play_again()
                return answer
            else:
                shorter_list.remove(player_input)

            if len(shorter_list) == 2:
                print("Game oveeer!")
                answer = ask_to_play_again()
                return answer


def filter_list(lucky_list, lucky_number):
    minimum_value = lucky_number - 10
    maximum_value = lucky_number + 10

    shorter_list = []

    for element in lucky_list:
        if element >= minimum_value and element <= maximum_value:
            shorter_list.append(element)

    return shorter_list


"""
Main loop
"""


def Main():
    print("Hi and welcome to the lucky numbers game!")
    player_name = get_player_name()
    while True:
        player_birthdate = get_player_birthdate()
        player_age = calculate_age(player_birthdate)

        if player_age >= 18:
            break
        else:
            print("You have to be 18 or older to play, try again!")

    while True:
        answer = play_round()
        if answer.startswith("y"):
            continue
        else:
            print("Thanks for playing!")
            break


Main()
