from src.guese_the_number import Computer, Comunication, PlayerGame, Game
from src.guese_the_number import Choosing
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
