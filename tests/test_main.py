from unittest.mock import patch
from src.main import handle_interaction

def test_time_command():
    with patch("src.tts.offline_tts.speak") as mock_speak:
        response = handle_interaction("time")
        assert "time is" in response
        mock_speak.assert_called_once_with(response)

def test_date_command():
    with patch("src.tts.offline_tts.speak") as mock_speak:
        response = handle_interaction("date")
        assert "date is" in response
        mock_speak.assert_called_once_with(response)

def test_unknown_command():
    with patch("src.tts.offline_tts.speak") as mock_speak:
        response = handle_interaction("foobar")
        assert "I don't understand" in response
        mock_speak.assert_called_once_with(response)

def test_exit_command():
    with patch("src.tts.offline_tts.speak") as mock_speak:
        response = handle_interaction("exit")
        assert "Goodbye" in response
        mock_speak.assert_called_once_with(response)
