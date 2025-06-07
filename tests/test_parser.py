# ------------------------------- Libraries ---------------------------
import pytest
from src.cli import parser


# ------------------------------- Tests ---------------------------


def test_handle_command_time():
    """Testing the parser returns a suitable reply for the given input
    """
    response = parser.handle_command("time")
    assert "time is" in response
    response = parser.handle_command("TIME")
    assert "time is" in response

def test_handle_command_date():
    """Testing the parser returns a suitable reply for the given input
    """
    response = parser.handle_command("date")
    assert "date is" in response
    response = parser.handle_command("DATE")
    assert "date is" in response

def test_handle_command_exit():
    """Testing the parser returns a suitable reply for the given input
    """
    response = parser.handle_command("exit")
    assert "Goodbye" in response
    response = parser.handle_command("EXIT")
    assert "Goodbye" in response

def test_handle_command_fail():
    """Testing the parser returns a suitable reply for the given input
    """
    response = parser.handle_command("foobar")
    assert "I don't understand" in response

def test_handle_command_without_argument():
    with pytest.raises(TypeError):
        parser.handle_command()