import random


class LuckyNumberRound:
    def __init__(self):
        self.lucky_list = []
        self.lucky_number = 0
        self.tries = 0

    def generate_lucky_list(self):
        lucky_list = []
        for i in range(9):
            random_number = random.randint(0, 100)
            lucky_list.append(random_number)
        self.lucky_list = lucky_list

    def generate_lucky_number(self):
        lucky_number = random.randint(0, 100)
        self.lucky_number = lucky_number

    def filter_list(self):
        minimum_value = self.lucky_number - 10
        maximum_value = self.lucky_number + 10
        shorter_list = []
        for element in self.lucky_list:
            if element >= minimum_value and element <= maximum_value:
                shorter_list.append(element)
        return shorter_list

    def ask_to_play_again(self):
        while True:
            user_play_again = input("Play again? (y/n)\n").lower()
            if user_play_again.startswith("y"):
                return user_play_again
            elif user_play_again.startswith("n"):
                return user_play_again
            else:
                print("Invalid input")

    def play_round(self):
        self.tries = 1
        self.generate_lucky_list()
        self.generate_lucky_number()

        while self.lucky_number in self.lucky_list:
            self.generate_lucky_number()

        self.lucky_list.append(self.lucky_number)

        print(f"Here is the lucky list! {self.lucky_list}")

        # Validating userinput in loop
        while True:
            try:
                player_input = int(input("which is the lucky number?\n"))
                break
            except ValueError:
                print("Invalid number, please try again")

        if player_input == self.lucky_number:
            print(
                f"Congrats, game is over! And you got lucky number from: {self.tries} :)"
            )
            answer = self.ask_to_play_again()
            return answer
        else:
            shorter_list = self.filter_list()
            while True:
                self.tries += 1
                print(f"\nTry number: {self.tries}")
                print(f"New list is: {shorter_list}")
                # Validating userinput
                try:
                    player_input = int(input("choose the lucky number?\n"))
                except ValueError:
                    print("Input a valid number")
                    continue
                if player_input == self.lucky_number:
                    print(
                        f"Congrats, game is over! And you got lucky number from: {self.tries} :)"
                    )
                    answer = self.ask_to_play_again()
                    return answer
                # If player_input is not in shorter_list
                if player_input not in shorter_list:
                    print("Number is not in list, try again")
                    continue
                # Wrong guess but in list
                shorter_list.remove(player_input)
                print(f"{player_input} was removed from list")

                if len(shorter_list) == 2:
                    print("Game oveeer!")
                    answer = self.ask_to_play_again()
                    return answer
