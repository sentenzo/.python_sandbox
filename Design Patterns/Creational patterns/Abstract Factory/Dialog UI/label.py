from abc import ABC, abstractmethod

class Label(ABC):
    def __init__(self, text) -> None:
        self.text = text
    @abstractmethod
    def render(self): pass

class WindowsLabel(Label):
    def render(self):
        print(f"Rendering Windows Label with \"{self.text}\"")

class WebLabel(Label):
    def render(self):
        print(f"Rendering Web Label with \"{self.text}\"")

class MacLabel(Label):
    def render(self):
        print(f"Rendering Mac Label with \"{self.text}\"") 