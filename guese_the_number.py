import random
import sys


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


class Computer:
    def set_computer_number(self):
        return random.randint(0, 100)


class Game:
    def __init__(self):
        self._history: list = []
        self._TRIES: int = 10

    def guess_number_user_mod(self, computer_number):
        while self._TRIES > 0:
            _user_answer_str: str = input("Your number? ").strip()

            if not _user_answer_str:
                print("Empty, please try again!")
                continue

            if not _user_answer_str.isdigit():
                print("Only numbers are allowed! Try again.")
                continue

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
        self._TRIES = 10
        print("❌ You ran out of tries! Game over.")

    def guess_number_computer_mod(self, user_number: int):
        computer_guess = 0
        start_point = 0
        end_point = 100
        while self._TRIES > 0:
            computer_guess = random.randint(start_point, end_point)
            if computer_guess > user_number:
                print("I did'nt guess it, ir's less.")
                end_point = computer_guess
            elif computer_guess < user_number:
                print("I did'nt guess it, ir's higher.")
                start_point = computer_guess
            else:
                print("🎉 I win")
        self._TRIES = 10
        print("❌ You ran out of tries! Game over.")


class ComputerGame:
    def __init__(self, computer: Computer, game: Game):
        self.computer = computer
        self.game = game

    def computer_play(self):
        while True:
            while True:
                try:
                    self.number: str = int(
                        input("What number do you want to set beetween 0 and 100? "))
                except TypeError:
                    print("Only numbers")
                if not self.number:
                    print("Enter something")
                elif self.number == "q":
                    return
                elif self.number < 0 or self.number > 100:
                    print("Only this range 0-100")
                else:
                    break
            self.game.guess_numbe_computer_mod(self.number)
            _checker: str = input("Do you want to play again? y or n: ")
            if _checker == "y":
                continue
            elif _checker == "n":
                print("Okay, have a good day!")
                break
            else:
                print("Wrong type of data!")
                break


class PlayerGame:
    def __init__(self, computer: Computer, game: Game):
        self.computer = computer
        self.game = game

    def player_play(self):
        while True:
            self.number: int = self.computer.set_computer_number()
            self.game.guess_number_computer_mod(self.number)
            _checker: str = input("Do you want to play again? y or n: ")
            if _checker == "y":
                continue
            elif _checker == "n":
                print("Okay, have a good day!")
                break
            else:
                print("Wrong type of data!")
                break


class Choosing:
    def __init__(self, user_message: Comunication):
        self.user_messager = user_message

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
    computer_game = ComputerGame(computer, game)
    player_game = PlayerGame(computer, game)
    app = GuessGame(user_message, computer, chose, player_game, computer_game)
    app.run()


if __name__ == "__main__":
    main()
