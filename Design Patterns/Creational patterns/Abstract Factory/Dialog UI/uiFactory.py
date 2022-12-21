from button import Button
from label import Label
from abc import ABC, abstractmethod
from typing import Any, Callable

class UiFactory(ABC):
    @abstractmethod
    def createLabel(self, text: str, ) -> Label: pass
    @abstractmethod
    def createButton(self, btnText: str
					 , doOnClick: Callable[[], Any]) -> Button: pass

class UiFactory_Windows(UiFactory):
    def createLabel(self, text: str, ) -> Label:
        return Label.WindowsLabel(text)
    def createButton(self, btnText: str
					 , doOnClick: Callable[[], Any]) -> Button:
        return Button.WindowsButton(btnText, doOnClick)

class UiFactory_Web(UiFactory):
    def createLabel(self, text: str, ) -> Label:
        return Label.WebLabel(text)
    def createButton(self, btnText: str
					 , doOnClick: Callable[[], Any]) -> Button:
        return Button.WebButton(btnText, doOnClick)

class UiFactory_Mac(UiFactory):
    def createLabel(self, text: str, ) -> Label:
        return Label.MacLabel(text)
    def createButton(self, btnText: str
					 , doOnClick: Callable[[], Any]) -> Button:
        return Button.MacButton(btnText, doOnClick)