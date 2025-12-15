class Player:
    def __init__(self):
        self.player_name = ""
        self.player_birthdate = ""
        self.player_age = 0
        self.current_year = 2022

    def input_player_name(self):
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
                print("You must provide exactly firstname and lastname")
                continue

            break
        self.player_name = player_name

    def get_player_birthdate(self):
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
                        print("Only leap year for february has 29 days")
                        continue
                elif day > 29:
                    print("February only has 28 days if not leap year")
                    continue

            player_birthdate = input_date
            self.player_birthdate = player_birthdate
            break

    def calculate_age(self):
        year = int(self.player_birthdate[:4])
        self.player_age = self.current_year - year

    def is_adult(self):
        return self.player_age >= 18
