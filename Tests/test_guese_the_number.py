from src.guese_the_number import Computer, Comunication, PlayerGame, Game
from src.guese_the_number import Choosing, ComputerGame
import pytest


class TestComputer:
    @pytest.fixture
    def obj(self):
        return Computer()

    def test_computer_number(self, obj):
        result = obj.set_computer_number()
        assert result > 0 and result < 100


class TestComunication:
    @pytest.fixture
    def obj(self):
        return Comunication()

    def test_hi(self, obj, capsys):
        obj.say_hi()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Welcome! This is a game where you need to guess the number.\n" + \
            "Number is between 0 and 100. You have 10 tries. Type 'q' to quit."

    def test_bye(self, obj, capsys):
        obj.say_bye()
        captured = capsys.readouterr()
        assert captured.out.strip() == obj._bye_words


class TestChossing:
    @pytest.fixture
    def obj(self):
        user_message = Comunication()
        return Choosing(user_message)

    def test_chossing(self, obj, capsys, monkeypatch):
        inputs = iter(["1", "2"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        choise = obj.chose_the_mode()
        captured = capsys.readouterr()
        assert choise == 1 or choise == 2
        assert "Avaibale operations" in captured.out

    def test_invalid_then_valid_choice(self, obj, monkeypatch, capsys):
        inputs = iter(["", "x", "2"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        choice = obj.chose_the_mode()
        captured = capsys.readouterr()

        assert choice == 2
        assert "It's empty, try again!" in captured.out
        assert "Only numbers" in captured.out

    def test_quit_option(self, obj, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", lambda _: "q")
        with pytest.raises(SystemExit):
            obj.chose_the_mode()

        captured = capsys.readouterr()
        assert "Thank you for using this app" in captured.out


class TestPlayerGame:
    class FakeComputerNumber:
        def set_computer_number(self):
            return 10

    class FakeGame:
        def guess_number_user_mod(self, number):
            print(f"It was called with {number}")

    def test_player_game_exit(self, capsys, monkeypatch):
        inputs = iter(["n"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        fake_computer = self.FakeComputerNumber()
        fake_game = self.FakeGame()
        player = PlayerGame(fake_computer, fake_game)
        player.player_play()
        output = capsys.readouterr().out
        assert "It was called with 10" in output
        assert "Okay, have a good day!" in output

    def test_player_game_repeat(self, capsys, monkeypatch):
        inputs = iter(["y", ""])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        fake_computer = self.FakeComputerNumber()
        fake_game = self.FakeGame()
        player = PlayerGame(fake_computer, fake_game)
        player.player_play()
        output = capsys.readouterr().out
        assert "It was called with 10" in output
        assert not "Okay, have a good day!" in output
        assert "Wrong type of data!" in output


class TestComputerGame:
    class FakeGame:
        def guess_number_computer_mod(self, number):
            number = 15
            print(f"App has worked with {number}")

    def test_computer_game(self, capsys, monkeypatch):
        inputs = iter(["fgh", "", "15", "y", "150", "15", "fdetw", "15", "n"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        game = self.FakeGame()
        computer = ComputerGame(game)
        computer.computer_play()
        output = capsys.readouterr().out

        assert "Only numbers" in output
        assert "Enter something" in output
        assert "App has worked with 15" in output
        assert "Only this range 0-100" in output
        assert "Wrong type of data!" in output


class TestGame:
    @pytest.fixture
    def number(self):
        return 79

    def test_guess_number_user_mod(self, number, capsys, monkeypatch):
        inputs = iter(["", "gfjg", "15", "85", "79", "", "15", "n",
                       "79", "y"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        game = Game()
        game.guess_number_user_mod(number)
        output = capsys.readouterr().out
        assert "Empty, please try again!" in output
        assert "Only numbers are allowed! Try again." in output
        assert "Too low! You have 9 tries left." in output
        assert "Too high! You have 8 tries left." in output
        assert "🎉 Congratulations, you guessed it!" in output
        assert "Wrong answer!" in output
        assert "Only leters" in output
        assert "You guese it for 2 times" in output

    def test_guess_number_computer_mod(self, number, capsys, monkeypatch):
        guesses = iter([30, 50, 79])
        monkeypatch.setattr("random.randint", lambda start, end: next(guesses))

        inputs = iter(["n"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        game = Game()
        game.guess_number_computer_mod(number)

        out = capsys.readouterr().out
        assert "My number is: 30" in out
        assert "My number is: 50" in out
        assert "Your number is 79 🎉 I win" in out
