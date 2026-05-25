import tempfile
from pathlib import Path
from jarviscli.plugins.dictionary import dictionary
from jarviscli.plugins.location import location
from jarviscli.plugins.clock import timer
from jarviscli.plugins.qr_generator import QRGenerator


class FakeJarvis:
    def __init__(self):
        self.outputs = []

    def say(self, text, color="", speak=True):
        self.outputs.append(str(text))
        print(str(text))

    def input(self, prompt="", color=""):
        print(prompt)
        return ""


fake = FakeJarvis()
print("---DICTIONARY---")
dictionary(fake, "test")
print("---LOCATION---")
location(fake, "")
print("---TIMER---")
timer(fake, "1s")
print("---QR---")


class QRJarvis(FakeJarvis):
    def __init__(self):
        super().__init__()
        self.inputs = iter([
            "https://github.com",
            str(Path(tempfile.gettempdir())),
            "test_qr",
        ])

    def input(self, prompt="", color=""):
        print(prompt)
        return next(self.inputs)

    def spinner_start(self, message="Starting "):
        print("spinner start", message)

    def spinner_stop(self, message="Task executed successfully! ", color=""):
        print("spinner stop", message)


QRGenerator()(QRJarvis(), "")
print("VERIFIED")
