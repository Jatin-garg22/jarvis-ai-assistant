import webbrowser
from urllib.parse import quote_plus

from plugin import plugin

try:
    import speech_recognition as sr
except ImportError:
    sr = None


def _clean_youtube_query(query):
    stop_words = {
        'youtube', 'on', 'a', 'song', 'video',
        'open', 'launch', 'play', 'search', 'for'
    }
    cleaned_words = [
        word for word in query.lower().split()
        if word not in stop_words
    ]
    return ' '.join(cleaned_words).strip()


def _listen_for_youtube_query():
    if sr is None:
        return None

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            return recognizer.recognize_google(audio).strip()
    except (AttributeError, OSError, sr.UnknownValueError, sr.RequestError):
        return None


@plugin('play')
def play(jarvis, s):
    query = (s or '').strip()

    if not query and sr is not None:
        jarvis.say('Speak your YouTube request now.')
        query = _listen_for_youtube_query()

    if not query:
        webbrowser.open('https://www.youtube.com')
        jarvis.say('Opening YouTube.')
        return

    search_query = _clean_youtube_query(query)

    if not search_query:
        webbrowser.open('https://www.youtube.com')
        jarvis.say('Opening YouTube.')
        return

    webbrowser.open(
        'https://www.youtube.com/results?search_query=' +
        quote_plus(search_query)
    )
    jarvis.say('Searching YouTube for {}'.format(search_query))
