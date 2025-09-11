import random


class GuessGame:
    def say_hi(self):
        print("Welcome! This is a game where you need to guess the number.")
        print("Number is between 0 and 100. You have 10 tries. Type 'q' to quit.\n")

    def set_computer_number(self):
        return random.randint(0, 100)

    def guess_number(self, computer_number):
        TRIES = 10
        while TRIES > 0:
            user_answer_str = input("Your number? ").strip()

            if not user_answer_str:
                print("Empty, please try again!")
                continue

            if user_answer_str.lower() == "q":
                print("Exit the game!")
                return

            if not user_answer_str.isdigit():
                print("Only numbers are allowed! Try again.")
                continue

            user_answer = int(user_answer_str)

            if user_answer > computer_number:
                TRIES -= 1
                print(f"Too high! You have {TRIES} tries left.")
            elif user_answer < computer_number:
                TRIES -= 1
                print(f"Too low! You have {TRIES} tries left.")
            else:
                print("🎉 Congratulations, you guessed it!")
                return

        print("❌ You ran out of tries! Game over.")


def main():
    app = GuessGame()
    app.say_hi()
    number = app.set_computer_number()
    app.guess_number(number)


if __name__ == "__main__":
    main()

