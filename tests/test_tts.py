# ------------------------------- Libraries ---------------------------
from unittest.mock import patch    # Using mock to prevent audio output
import pytest
from src.tts import offline_tts


# ------------------------------- Tests ---------------------------

def test_speak_valid_text():
    """Testing correct output"""
    with patch.object(offline_tts.engine, "say") as mock_say, \
         patch.object(offline_tts.engine, "runAndWait") as mock_run:
        
        offline_tts.speak("Hello, world!")
        
        mock_say.assert_called_once_with("Hello, world!")
        mock_run.assert_called_once()

def test_speak_empty_text_raises():
    with pytest.raises(ValueError):
        offline_tts.speak("")