from LuckyNumberRound import LuckyNumberRound
from Player import Player


class Game:
    def __init__(self):
        self.player = Player()

    def play(self):
        print("Hi and welcome to the lucky numbers game!")

        # Name input
        self.player.input_player_name()
        # Birthday input
        self.player.get_player_birthdate()
        # Age validation
        self.player.calculate_age()

        while not self.player.is_adult():
            print("You are not old enough to play")
            self.player.get_player_birthdate()
            self.player.calculate_age()

        # Main game loop
        while True:
            one_round = LuckyNumberRound()
            answer = one_round.play_round()

            if answer.startswith("y"):
                continue
            else:
                print("Thank you for playing, hope to see you again!")
                break
