from time import ctime, sleep

from colorama import Fore

from plugin import plugin


def parse_duration(duration):
    duration = duration.strip().lower()
    if not duration:
        raise ValueError("duration is required")

    if duration.isdigit():
        return int(duration)

    total_seconds = 0
    current_number = ""

    for character in duration:
        if character.isdigit():
            current_number += character
            continue

        if character not in ["h", "m", "s"]:
            raise ValueError("invalid duration format")

        if not current_number:
            raise ValueError("invalid duration format")

        value = int(current_number)
        if character == "h":
            total_seconds += value * 3600
        elif character == "m":
            total_seconds += value * 60
        else:
            total_seconds += value
        current_number = ""

    if current_number:
        raise ValueError("invalid duration format")

    if total_seconds <= 0:
        raise ValueError("duration must be greater than zero")

    return total_seconds


def run_countdown(jarvis, total_seconds):
    while total_seconds > 0:
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        if hours:
            label = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        else:
            label = "{:02d}:{:02d}".format(minutes, seconds)

        jarvis.say("Timer: {}".format(label), Fore.CYAN)
        sleep(1)
        total_seconds -= 1

    jarvis.say("Time is up!", Fore.GREEN)


@plugin("clock")
def clock(jarvis, s):
    """Gives information about time"""
    jarvis.say(ctime(), Fore.BLUE)


@plugin("stopwatch")
def stopwatch(jarvis, s):
    """
    Start stopwatch

    L       Lap
    R       Reset
    SPACE   Pause
    Q       Quit
    """
    jarvis.say("Stopwatch is not available in this environment.")


@plugin("timer")
def timer(jarvis, s):
    """
    Set a timer

    Usages:

    timer 10
    timer 1h5m30s
    """
    if not s or not s.strip():
        jarvis.say("Please specify duration")
        return

    try:
        total_seconds = parse_duration(s)
    except ValueError:
        jarvis.say("Please use a valid duration like 10, 30s, 2m, or 1h5m30s")
        return

    run_countdown(jarvis, total_seconds)
