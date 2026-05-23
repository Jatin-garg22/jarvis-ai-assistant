from unittest.mock import MagicMock, patch

from plugins.play import play
from tests import PluginTest


class PlayTest(PluginTest):
    def setUp(self):
        self.test = self.load_plugin(play)

    @patch('plugins.play.webbrowser.open')
    @patch('plugins.play.sr')
    def test_play_uses_voice_input_when_query_is_empty(self, mock_sr, mock_open):
        mock_recognizer = MagicMock()
        mock_recognizer.recognize_google.return_value = 'open youtube'
        mock_sr.Recognizer.return_value = mock_recognizer
        mock_sr.Microphone.return_value.__enter__.return_value = MagicMock()

        self.test.run('')

        mock_open.assert_called_once_with('https://www.youtube.com')
        self.assertEqual(self.history_say().last_text(), 'Opening YouTube.')

    @patch('plugins.play.webbrowser.open')
    @patch('plugins.play.sr')
    def test_play_uses_voice_query_as_search_term(self, mock_sr, mock_open):
        mock_recognizer = MagicMock()
        mock_recognizer.recognize_google.return_value = 'cats and dogs'
        mock_sr.Recognizer.return_value = mock_recognizer
        mock_sr.Microphone.return_value.__enter__.return_value = MagicMock()

        self.test.run('')

        mock_open.assert_called_once_with(
            'https://www.youtube.com/results?search_query=cats+and+dogs'
        )
        self.assertEqual(
            self.history_say().last_text(),
            'Searching YouTube for cats and dogs'
        )
