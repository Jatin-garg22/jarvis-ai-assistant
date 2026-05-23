import os
import sys
import webbrowser

from plugin import plugin


URL_SHORTCUTS = {
    'youtube': 'https://www.youtube.com',
    'linkedin': 'https://www.linkedin.com',
    'chatgpt': 'https://chatgpt.com',
    'google': 'https://www.google.com',
    'gmail': 'https://mail.google.com'
}


@plugin('open')
def open(jarvis, s):
    query = (s or '').strip().lower()
    normalized = query.replace('linkdien', 'linkedin')

    if normalized in URL_SHORTCUTS:
        webbrowser.open(URL_SHORTCUTS[normalized])
        return

    if normalized == '':
        jarvis.say('Available shortcuts: youtube, linkedin, chatgpt, google, gmail')
        if sys.platform.startswith('linux'):
            jarvis.say('On Linux, you can also open desktop apps by typing: open <appname>')
        return

    if sys.platform.startswith('linux'):
        string = "gtk-launch " + "/usr/share/applications/" + query + ".desktop"
        os.system(string)
        return

    jarvis.say('I can open website shortcuts like youtube, linkedin, chatgpt, google, or gmail.')
