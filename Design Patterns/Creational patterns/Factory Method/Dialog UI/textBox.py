from abc import ABC, abstractmethod

class TextBox(ABC):
    def __init__(self, text) -> None:
        self.text = text

    @abstractmethod
    def render(self): pass


class WindowsTextBox(TextBox):
    def render(self):
        print(f"Rendering Windows TextBox with \"{self.text}\"")


class WebTextBox(TextBox):
    def render(self):
        print(f"Rendering Web TextBox with \"{self.text}\"")

class MacTextBox(TextBox):                                   # ++
    def render(self):                                        # ++
        print(f"Rendering Mac TextBox with \"{self.text}\"") # ++