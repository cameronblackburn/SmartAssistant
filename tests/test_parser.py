# ------------------------------- Libraries ---------------------------
from src.cli import parser


# ------------------------------- Tests ---------------------------


def test_handle_commands():
    """Testing correct output for time"""
    response = parser.handle_command("time")
    assert "time is" in response
    response = parser.handle_command("TIME")
    assert "time is" in response
    response = parser.handle_command("date")
    assert "date is" in response
    response = parser.handle_command("DATE")
    assert "date is" in response
    response = parser.handle_command("exit")
    assert "Goodbye" in response
    response = parser.handle_command("EXIT")
    assert "Goodbye" in response
    response = parser.handle_command("rrr")
    assert "I don't understand" in response
