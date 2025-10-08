# Imports
import random
import sys
import time

# static valuables
START_POINT = 0
END_POINT = 100

# Comunicate with user


class Comunication:
    def __init__(self,
                 hi_words="Welcome! This is a game where you need to guess the number.",
                 explanation_words="Number is between 0 and 100. You have 10 tries. Type 'q' to quit.\n",
                 bye_words="Thank you for using this app!"):
        self._hi_words: str = hi_words
        self._explanaition: str = explanation_words
        self._bye_words: str = bye_words

    def say_hi(self) -> str:
        print(self._hi_words)
        print(self._explanaition)

    def say_bye(self) -> str:
        print(self._bye_words)

# Set special computer number


class Computer:
    def set_computer_number(self) -> int:
        return random.randint(START_POINT, END_POINT)

# Game


class Game:
    def __init__(self):
        self._history: list = []
        self._TRIES: int = 10

    def guess_number_user_mod(self, computer_number):
        while self._TRIES > 0:
            _user_answer_str: str = input("Your number? ").strip()

            if not _user_answer_str:
                print("Empty, please try again!")

            if not _user_answer_str.isdigit():
                print("Only numbers are allowed! Try again.")

            _user_answer: int = int(_user_answer_str)

            if _user_answer > computer_number:
                self._TRIES -= 1
                self._history.append(_user_answer)
                print(f"Too high! You have {self._TRIES} tries left.")
            elif _user_answer < computer_number:
                self._TRIES -= 1
                self._history.append(_user_answer)
                print(f"Too low! You have {self._TRIES} tries left.")
            else:
                print("🎉 Congratulations, you guessed it!")
                _user_input: str = input(
                    "Do you want to see a history? y(yes)/n(no)")
                if not _user_input:
                    print("Wrong answer!")
                if _user_input.isdigit():
                    print("Only leters")
                if _user_input.lower() == "n":
                    self._history.clear()
                    return print(f"You guese it for {10 - self._TRIES} times")
                if _user_input.lower() == "y":
                    return print(self._history)
        self._TRIES: int = 10
        print("❌ You ran out of tries! Game over.")

    def guess_number_computer_mod(self, user_number: int):
        # points for guessing
        _computer_guess: int = 0
        _start_point: int = 0
        _end_point: int = 100
        while self._TRIES > 0:
            _computer_guess: int = random.randint(_start_point, _end_point)
            if _computer_guess > user_number:
                self._TRIES -= 1
                self._history.append(_computer_guess)
                print(
                    f"My number is: {_computer_guess}. I didn't guess it, it's less.")
                _end_point = _computer_guess
                time.sleep(5)
            elif _computer_guess < user_number:
                self._TRIES -= 1
                self._history.append(_computer_guess)
                print(
                    f"My number is: {_computer_guess}. I didn't guess it, it's higher.")
                _start_point = _computer_guess
                time.sleep(5)
            else:
                print(f"Your number is {user_number} 🎉 I win")
                _user_input: str = input(
                    "Do you want to see a history? y(yes)/n(no)")
                if not _user_input:
                    print("Wrong answer!")
                if _user_input.isdigit():
                    print("Only leters")
                if _user_input.lower() == "n":
                    self._history.clear()
                    return print(f"You guese it for {10 - self._TRIES} times")
                if _user_input.lower() == "y":
                    return print(self._history)

        self._TRIES = 10
        print("❌ You ran out of tries! Game over.")

# Computer mode game


class ComputerGame:
    def __init__(self, game: Game):
        self.game = game

    def computer_play(self):
        while True:
            while True:
                number: str = input(
                    "What number do you want to set beetween 0 and 100? ")
                if number.isalpha():
                    print("Only numbers")
                    continue
                elif not number:
                    print("Enter something")
                    continue
                elif int(number) < 0 or int(number) > 100:
                    print("Only this range 0-100")
                    continue
                else:
                    break
            number = int(number)
            self.game.guess_number_computer_mod(number)
            _checker: str = input("Do you want to play again? y or n: ")
            if _checker == "y":
                continue
            elif _checker == "n":
                print("Okay, have a good day!")
                break
            else:
                print("Wrong type of data!")
                break

# Player mode game


class PlayerGame:
    def __init__(self, computer: Computer, game: Game):
        self.computer = computer
        self.game = game

    def player_play(self):
        while True:
            self.number: int = self.computer.set_computer_number()
            self.game.guess_number_user_mod(self.number)
            _checker: str = input("Do you want to play again? y or n: ")
            if _checker == "y":
                continue
            elif _checker == "n":
                print("Okay, have a good day!")
                break
            else:
                print("Wrong type of data!")
                break

# Chosse the operation


class Choosing:
    def __init__(self, user_message: Comunication):
        self.user_messager = user_message

    # chosse mod
    def chose_the_mode(self):
        operations: dict = {
            1: "You guess",
            2: "Computer guess"
        }
        print("\n Avaibale operations:")
        for key, value in operations.items():
            print(f"{key}: {value}")
        while True:
            user_answer_str: str = input("Chose the mod for game: ")
            if not user_answer_str:
                print("It's empty, try again!")
            elif user_answer_str == "q":
                self.user_messager.say_bye()
                sys.exit()
            elif user_answer_str.isalpha():
                print("Only numbers")
            else:
                user_answer: int = int(user_answer_str)
                if user_answer not in operations:
                    print("There is no such option. Try again")
                else:
                    return user_answer


class GuessGame:
    def __init__(self, user_message: Comunication, computer: Computer,
                 chose: Choosing, player_game: PlayerGame, computer_game: ComputerGame):
        self.chose = chose
        self.user_message = user_message
        self.computer = computer
        self.player_game = player_game
        self.computer_game = computer_game

    # APP
    def run(self):
        self.user_message.say_hi()
        answer = self.chose.chose_the_mode()
        if answer == 1:
            self.player_game.player_play()
        else:
            self.computer_game.computer_play()
        self.user_message.say_bye()


def main():
    user_message = Comunication()
    chose = Choosing(user_message)
    computer = Computer()
    game = Game()
    computer_game = ComputerGame(game)
    player_game = PlayerGame(computer, game)
    app = GuessGame(user_message, computer, chose, player_game, computer_game)
    app.run()


if __name__ == "__main__":
    main()
