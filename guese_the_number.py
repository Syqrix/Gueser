import random


class Comunication:
    def __init__(self,
                 text1="Welcome! This is a game where you need to guess the number.",
                 text2="Number is between 0 and 100. You have 10 tries. Type 'q' to quit.\n"):
        self.hi_words: str = text1
        self.explanaition: str = text2

    def say_hi(self):
        print(self.hi_words)
        print(self.explanaition)


class Computer:
    def set_computer_number(self):
        return random.randint(0, 100)


class Guesser:
    def __init__(self):
        self.history: list = []
        self.TRIES: int = 10

    def guess_number(self, computer_number):
        while self.TRIES > 0:
            user_answer_str: str = input("Your number? ").strip()

            if not user_answer_str:
                print("Empty, please try again!")
                continue

            if not user_answer_str.isdigit():
                print("Only numbers are allowed! Try again.")
                continue

            user_answer: int = int(user_answer_str)

            if user_answer > computer_number:
                self.TRIES -= 1
                self.history.append(user_answer)
                print(f"Too high! You have {self.TRIES} tries left.")
            elif user_answer < computer_number:
                self.TRIES -= 1
                self.history.append(user_answer)
                print(f"Too low! You have {self.TRIES} tries left.")
            else:
                print("🎉 Congratulations, you guessed it!")
                user_input: str = input(
                    "Do you want to see a history? y(yes)/n(no)")
                if not user_input:
                    print("Wrong answer!")
                if user_input.isdigit():
                    print("Only leters")
                if user_input.lower() == "n":
                    self.history.clear()
                    return print(f"You guese it for {10 - self.TRIES} times")
                if user_input.lower() == "y":
                    return print(self.history)
        self.TRIES = 10
        print("❌ You ran out of tries! Game over.")


class GuessGame:
    def __init__(self, user_message: Comunication, computer: Computer, gueser: Guesser):
        self.user_message = user_message
        self.computer = computer
        self.gueser = gueser

    def run(self):
        self.user_message.say_hi()
        while True:
            self.number: int = self.computer.set_computer_number()
            self.gueser.guess_number(self.number)
            checker: str = input("Do you want to play again? y or n: ")
            if checker == "y":
                continue
            elif checker == "n":
                print("Okay, have a good day!")
                break
            else:
                print("Wrong type of data!")
                break


def main():
    user_message = Comunication()
    computer = Computer()
    gueser = Guesser()
    app = GuessGame(user_message, computer, gueser)
    app.run()


if __name__ == "__main__":
    main()
