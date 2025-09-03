import random


class Guese:

    def say_hi(self):
        print("Welcome this is game. You need to guese the number.")

    def set_computer_number(self):
        self.computer_number = random.randint(0, 100)
        print("Number should be between 0 to 100 or q to leave. You have 10 tries.\n")
        return self.computer_number

    def guese(self, computer_number):
        TRIES = 10
        while True:
            user_answer_str = input("Your number? ")
            if not user_answer_str:
                print("Empty, please try again!")
                continue

            if user_answer_str.lower() == "q":
                return None

            if user_answer_str.isdigit():
                user_answer = int(user_answer_str)
            else:
                print("Only number! Try again.")
                continue

            if TRIES == 0:
                print("End of game! You are lose!")
                return None

            if user_answer > computer_number:
                TRIES -= 1
                print(f"No, it less! You have {TRIES} yet.")
                continue
            elif user_answer < computer_number:
                TRIES -= 1
                print(f"No, it bigger! You have {TRIES} yet.")
                continue
            else:
                print("Congratulations, you win!")
                break


def main():
    app = Guese()
    app.say_hi()
    computer_number = app.set_computer_number()
    answer = app.guese(computer_number)
    if answer is None:
        print("Exit the app!")


if __name__ == "__main__":
    main()
