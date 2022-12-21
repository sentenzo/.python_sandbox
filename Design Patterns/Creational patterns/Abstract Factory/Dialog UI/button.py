from abc import ABC, abstractmethod
from typing import Any, Callable

class Button(ABC):
    def __init__(self, btnText: str, doOnClick: Callable[[], Any]) -> None:
        self.btnText = btnText
        self.doOnClick = doOnClick
    @abstractmethod
    def render(self) -> None: pass
    def onClick(self) -> None:
        self.doOnClick()

class WindowsButton(Button):
    def render(self):
        print(f"Rendering Windows button titled \"{self.btnText}\"")

class WebButton(Button):
    def render(self):
        print(f"Rendering Web button titled \"{self.btnText}\"")

class MacButton(Button):
    def render(self):
        print(f"Rendering Mac button titled \"{self.btnText}\"")
