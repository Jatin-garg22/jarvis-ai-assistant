import sys
from unittest.mock import patch

sys.path.insert(0, 'jarviscli')
from Jarvis import Jarvis

j = Jarvis()
plugins = sorted(j._plugin_manager.get_plugins().keys())
print('PLUGIN_COUNT', len(plugins))
print('PLUGINS', plugins)
print('PARSE_OPEN', j.parse_input('open youtube'))
print('PARSE_PLAY', j.parse_input('play a song on youtube'))
print('PARSE_WEATHER', j.parse_input('weather'))

with patch('webbrowser.open') as open_mock:
    j.do_open('youtube')
    print('OPEN_CALLS', open_mock.call_args_list)

with patch('webbrowser.open') as open_mock:
    j.do_play('a song on youtube')
    print('PLAY_CALLS', open_mock.call_args_list)
